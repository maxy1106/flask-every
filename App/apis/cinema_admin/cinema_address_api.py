from flask import g
from flask_restful import Resource, reqparse, fields, abort, marshal

from App.apis.api_constant import HTTP_OK
from App.apis.cinema_admin.utils import required_permmsion
from App.modeles.cinema_admin.cinema_address_model import CinemaAddress
from App.modeles.cinema_admin.permission_constant import PREMISSION_WRITE

parse = reqparse.RequestParser()
parse.add_argument("name",required=True,help="请输入影院名")
parse.add_argument("city",required=True,help="请输入影院城市")
parse.add_argument("district",required=True,help="请输入影院区域")
parse.add_argument("address",required=True,help="请输入影院地址")
parse.add_argument("phone",required=True,help="请输入影院电话")

cinema_address_fields = {
    "c_user":fields.Integer,
    "name":fields.String,
    "city":fields.String,
    "district":fields.String,
    "address":fields.String,
    "phone":fields.String,
    "score":fields.Float,
    "hallnum":fields.Integer,
    "servicechargs":fields.Float,
    "astrict":fields.Float,
    "flag":fields.Boolean,
}

single_cinema_address_fields = {
    "msg":fields.String,
    "status":fields.Integer,
    "data":fields.Nested(cinema_address_fields)
}

class CinemaAddressesResource(Resource):
    def get(self):
        return {"msg":"ok"}

    @required_permmsion(PREMISSION_WRITE)
    def post(self):
        args = parse.parse_args()
        name = args.get("name")
        city = args.get("city")
        district = args.get("district")
        address = args.get("address")
        phone = args.get("phone")
        cinema_address = CinemaAddress()
        cinema_address.c_user = g.user.id
        cinema_address.name = name
        cinema_address.city = city
        cinema_address.district = district
        cinema_address.address = address
        cinema_address.phone = phone

        if not cinema_address.save():
            abort(400,msg = "cinema can't save")

        data = {
            "msg":"create cinema success",
            "status":HTTP_OK,
            "data":cinema_address
        }
        return marshal(data,single_cinema_address_fields)

class CinemaAddressResource(Resource):
    def get(self,id):
        return {"msg":"ok"}

    def put(self,id):
        return {"msg": "ok"}


    def patch(self,id):
        return {"msg": "ok"}

    def delete(self,id):
        return {"msg": "ok"}