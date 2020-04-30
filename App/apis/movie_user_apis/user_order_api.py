import datetime

from flask import g
from flask_restful import Resource, reqparse, abort, fields, marshal

from App.apis.api_constant import HTTP_OK
from App.apis.movie_user_apis.utils import login_required, required_permmsion
from App.modeles.user.model_constant import VIP_USER, COMMON_USER
from App.modeles.user.movie_order_model import MovieOrder

parse = reqparse.RequestParser()
parse.add_argument("hall_movie_id",required = True,help="请提供排挡信息")
parse.add_argument("o_seats",required=True,help="请选择座位号")


movie_order_fields = {
    "o_price":fields.Float,
    "o_seats":fields.String,
    "o_hall_movie_id":fields.Integer,
    "o_status":fields.String,
    "o_user":fields.Integer
}

class MovieUserOrderResource(Resource):

    @login_required
    def post(self):
        user = g.user
        args = parse.parse_args()
        hall_movie_id = args.get("hall_movie_id")
        o_seats = args.get("o_seats")

        mover_order = MovieOrder()
        mover_order.o_hall_movie_id = hall_movie_id
        mover_order.o_seats = o_seats
        mover_order.o_user_id = user.id
        mover_order.o_time = datetime.datetime.now() + datetime.timedelta(minutes=15)

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