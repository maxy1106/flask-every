import datetime

from flask import g
from flask_restful import Resource, reqparse, abort, fields, marshal
from sqlalchemy.sql.elements import or_, and_

from App.apis.api_constant import HTTP_OK
from App.apis.movie_user_apis.utils import login_required, required_permmsion
from App.ext import db
from App.modeles.cinema_admin.cinema_hall_model import Hall
from App.modeles.cinema_admin.hall_movie_model import HallMovie
from App.modeles.user.model_constant import VIP_USER
from App.modeles.user.movie_order_model import MovieOrder, ORDER_STATUS_PAYED_NOT_GET, ORDER_STATUS_NOT_PAY, \
    ORDER_STATUS_GET

parse = reqparse.RequestParser()
parse.add_argument("hall_movie_id",required = True,help="请提供排挡信息")
parse.add_argument("o_seats",required=True,help="请选择座位号")


movie_order_fields = {
    "o_price":fields.Float,
    "o_seats":fields.String,
    "o_hall_movie_id":fields.Integer,
    "o_status":fields.String,
    "o_user_id":fields.Integer
}

class MovieUserOrderResource(Resource):

    @login_required
    def post(self):
        user = g.user
        args = parse.parse_args()
        hall_movie_id = args.get("hall_movie_id")
        o_seats = args.get("o_seats")

        """
        座位存在
        座位没有被锁单或者下单
        """
        #可用座位编号

        hall = Hall.query.get(HallMovie.query.get(hall_movie_id).h_id)

        movie_order_buyed = MovieOrder.query.filter(MovieOrder.o_hall_movie_id == hall_movie_id).filter(or_(MovieOrder.o_status == ORDER_STATUS_PAYED_NOT_GET,MovieOrder.o_status == ORDER_STATUS_GET)).all()

        movie_order_locked = MovieOrder.query.filter(MovieOrder.o_hall_movie_id == hall_movie_id).filter(and_(MovieOrder.o_status == ORDER_STATUS_NOT_PAY,MovieOrder.o_time > datetime.datetime.now())).all()

        print("movie_order_buyed",movie_order_buyed)
        print("movie_order_locked",movie_order_locked)

        seats_lock =[]

        for movie_order in movie_order_buyed:
            seats = movie_order.o_seats.split("#")

            seats_lock += seats

        for movie_order in movie_order_locked:
            seats = movie_order.o_seats.split("#")
            seats_lock += seats

        print("seats_lock",seats_lock)

        print("hall",hall)

        seats_can_buy = list(set(hall.h_seate.split("#")) ^ set(seats_lock))

        o_seats_list = o_seats.split("#")
        #判断当前选择的座位号是不是可选择座位号的子集
        if not set(o_seats_list).issubset(set(seats_can_buy)):
            abort("座位选择错误，请重新选择")
        #可用座位编号

        mover_order = MovieOrder()
        mover_order.o_hall_movie_id = hall_movie_id
        mover_order.o_seats = o_seats
        mover_order.o_user_id = user.id
        mover_order.o_time = datetime.datetime.now() + datetime.timedelta(minutes=15)


        '''
        try:
            movie_order1 = MovieOrder.query.get(1)
            movie_order2 = MovieOrder.query.get(2)
            db.session.delete(movie_order1)
            db.session.delete(movie_order2)
        except Exception as e:
            print(e)
            db.session.rollback()
            
        else:
            db.session.commit()
        '''

        if not mover_order.save():
            abort(400,msg="下单失败")

        data = {
            "msg":"下单成功",
            "status":HTTP_OK,
            "data":marshal(mover_order,movie_order_fields)
        }
        return data

class MovieUserOrdersResource(Resource):

    @required_permmsion(VIP_USER)
    def put(self,orderid):

        return {"msg":"oook"}