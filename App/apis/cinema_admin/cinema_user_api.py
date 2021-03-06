
from flask_restful import Resource, fields, abort, reqparse, marshal

from App.apis.api_constant import *
from App.apis.cinema_admin.cinema_user_utils import get_cinema_user
from App.apis.utils import  generator_cinema_user_token
from App.ext import cache
from App.modeles.cinema_admin.movie_admin_user import CinemaAdminUser


user_fields = {
    "username": fields.String,
    "phone": fields.String
}

single_user_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(user_fields),
    "token":fields.String
}

parse_base = reqparse.RequestParser()
parse_base.add_argument("password", type=str, required=True, help="请输入密码")
parse_base.add_argument("action", type=str, required=True, help="请确认请求参数")

parse_register = parse_base.copy()
parse_register.add_argument("username", type=str, required=True, help="请输入username")
parse_register.add_argument("phone", type=str, required=True, help="请输入手机号")

parse_login = parse_base.copy()
parse_login.add_argument("username", type=str, help="请输入username")
parse_register.add_argument("phone", type=str, help="请输入手机号")


class CinemaUsersResource(Resource):

    def post(self):
        args = parse_base.parse_args()
        password = args.get("password")
        action = args.get("action").lower()
        print("*************************************************************",action)

        if action == USER_ACTION_REGISTER:

            args_register = parse_register.parse_args()
            username = args_register.get("username")
            phone = args_register.get("phone")

            user_have = get_cinema_user(username) or get_cinema_user(phone)
            user = CinemaAdminUser()
            user.username = username
            user.password = password
            user.phone = phone

            if user_have:
                abort(400, msg="duplicate user")

            if not user.save():
                abort(400, msg="insert not success")

            token = generator_cinema_user_token()
            cache.set(token, user.id, 60 * 60 * 24 * 100)

            data = {
                "status": HTTP_OK,
                "msg": "insert success",
                "data": user,
                "token":token
            }
            return marshal(data,single_user_fields)
        elif action == USER_ACTION_LOGIN:

            args_login = parse_login.parse_args()
            username = args_login.get("username")
            phone = args_login.get("phone")

            user = get_cinema_user(username) or get_cinema_user(phone)
            print(user)

            if not user:
                abort(400, msg="该用户不存在")

            if not user.check_password(password):
                abort(401, msg="用户名或密码错误，请重新输入")

            if user.is_delete:
                abort(401, msg="用户不存在")

            token = generator_cinema_user_token()
            print("************************** token", token,type(token))
            print("******************* user.id",user.id)
            cache.set(token, user.id, 60 * 60 * 24 * 100)

            data = {
                "status": HTTP_OK,
                "msg": "login success%s" %username,
                "token": token
            }
            return data
        else:
            abort(400, msg="请提供正确参数")


class CinemaUserResource(Resource):
    def get(self, id):
        return {"msg": "user%d list" % id}
