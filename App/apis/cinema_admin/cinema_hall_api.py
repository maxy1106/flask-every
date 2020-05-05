from flask import g
from flask_restful import Resource, reqparse, abort, marshal, fields

from App.apis.api_constant import HTTP_OK
from App.apis.cinema_admin.utils import login_required, check_user_cinema
from App.modeles.cinema_admin.cinema_address_model import CinemaAddress
from App.modeles.cinema_admin.cinema_hall_model import Hall

parse = reqparse.RequestParser()
parse.add_argument("h_num",type = int,required = True,help="请输入hall 编号")
parse.add_argument("h_seats",required = True,help="请输入放映厅布局")
parse.add_argument("address_id",type = int,required = True,help="请输入影院")

hall_fields = {
    "id":fields.Integer,
    "h_address_id":fields.Integer,
    "h_num":fields.String,
    "h_seate":fields.String
}

class CinemaHallsResource(Resource):
    def get(self):
        return {"msg":"ok"}

    @login_required
    def post(self):

        args = parse.parse_args()
        h_num = args.get("h_num")
        h_seats = args.get("h_seats")
        address_id = args.get("address_id")

        cinema_user = g.user

        if not check_user_cinema(cinema_user,address_id):
            abort(403,msg = "该影院你没有权限修改")


        #这是上一个if 的替代版
        """       
        cinemas = CinemaAddress.query.filter(CinemaAddress.c_user == cinema_user.id).all()

        cinema_ids = []

        for cinema in cinemas:
            cinema_ids.append(cinema.id)

        if not address_id in cinema_ids:
            abort(403, msg="该影院你没有权限修改")
        """
        hall = Hall()
        hall.h_num = h_num
        hall.h_seate = h_seats
        hall.h_address_id = address_id

        if not hall.save():
            abort(403,msg="insert hall fail")

        data = {
            "msg":"insert hall success",
            "status":HTTP_OK,
            "data":marshal(hall,hall_fields)
        }

        return data

