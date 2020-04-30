from flask import request, g
from flask_restful import Resource, fields, marshal, reqparse, abort

from App.apis.admin_apis.utils import login_required
from App.apis.api_constant import HTTP_OK
from App.apis.cinema_admin.cinema_user_utils import get_cinema_user
from App.modeles.admin.admin_constant import PERMISSIONSETACTION, PERMISSIONADDACTION
from App.modeles.cinema_admin.cinema_address_model import CinemaAddress
from App.modeles.cinema_admin.movie_admin_user import CinemaAdminUser, Permissions, CinemaUserPermission
from App.modeles.cinema_admin.permission_constant import PREMISSION_READ, PREMISSION_WRITE

parse = reqparse.RequestParser()
parse.add_argument("is_verify",type = int,choices = [0,1],required = True,help="激活类型错误")

parse_post = reqparse.RequestParser()
parse_post.add_argument("action",required=True,help="请输入操作功能")
parse_post.add_argument("permissionname",choices = [PREMISSION_READ,PREMISSION_WRITE],required=True,help="请输入权限名称")

user_fields = {
    "id":fields.Integer,
    "username": fields.String,
    "phone": fields.String,
    "is_verify":fields.Boolean,
    "is_delete":fields.Boolean
}

single_user_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(user_fields),
}

mutil_user_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.List(fields.Nested(user_fields)),
}

cinema_user_permission_fields = {
    "c_user_id":fields.Integer,
    "c_permission_id":fields.Integer
}

class CinemasUsersResource(Resource):

    @login_required
    def get(self):

        cinema_users = CinemaAdminUser.query.all()

        data = {
            "msg":"get success",
            "status":HTTP_OK,
            "data":cinema_users
        }

        return marshal(data,mutil_user_fields)

    @login_required
    def post(self):
        args = parse_post.parse_args()
        action = args.get("action")
        permissionName = args.get("permissionname").lower()
        if action == PERMISSIONADDACTION:
            permission = Permissions()
            permission.p_name = permissionName
            if not permission.save():
                abort(403,msg = "insert permission error")

            data = {
                "msg":"insert permission success",
                "status":HTTP_OK,
                "data":permissionName
            }
            return data



class CinemasUserResource(Resource):

    @login_required
    def get(self,id):
        cinema_user = CinemaAdminUser.query.get(id)
        data = {
            "msg":"get success",
            "status":HTTP_OK,
            "data":cinema_user
        }

        return marshal(data,single_user_fields)

    @login_required
    def post(self,id):
        args = parse_post.parse_args()
        action = args.get("action")
        permissionName = args.get("permissionname").lower()
        if action == PERMISSIONSETACTION:
            cinema_user = get_cinema_user(id)

            if not cinema_user:
                abort(403,msg = "cinema user not exist")

            cinema_permission = Permissions.query.filter(Permissions.p_name.__eq__(permissionName)).first()
            if not cinema_permission:
                abort(403,msg="permission not exist")
            if cinema_user.check_permission(permissionName):
                abort(403,msg="user have this permission")
            cinema_user_permission = CinemaUserPermission()
            cinema_user_permission.c_user_id = cinema_user.id
            cinema_user_permission.c_permission_id = cinema_permission.id

            if not cinema_user_permission.save():
                abort(403,msg = "cinemaUserPermission not insert")

            data = {
                "msg":"cinema user permission insert success",
                "status":HTTP_OK,
                "data":marshal(cinema_user_permission,cinema_user_permission_fields)
            }

            return data

    @login_required
    def patch(self,id):

        cinema_user = CinemaAdminUser.query.get(id)
        args = parse.parse_args()

        is_verify = bool(args.get("is_verify"))

        cinema_user.is_verify = is_verify

        if not cinema_user.save():
            abort(400,msg="change fail")

        data = {
            "msg":"get success",
            "status":HTTP_OK,
            "data":cinema_user
        }

        return marshal(data,single_user_fields)
