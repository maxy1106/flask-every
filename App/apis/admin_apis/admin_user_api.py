import uuid

from flask_restful import Resource, fields, abort, reqparse, marshal

from App.apis.admin_apis.admin_user_utils import get_admin_user
from App.apis.api_constant import *
from App.apis.utils import generator_admin_user_token
from App.ext import cache
from App.modeles.admin.admin_user_model import AdminUser

user_fields = {
    "username": fields.String,
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
parse_base.add_argument("username", type=str, required=True, help="请输入username")



class AdminUsersResource(Resource):

    def post(self):
        args = parse_base.parse_args()
        password = args.get("password")
        action = args.get("action").lower()
        username = args.get("username")
        print("*************************************************************",action)

        if action == USER_ACTION_REGISTER:
            user_have = get_admin_user(username)
            user = AdminUser()
            user.username = username
            user.password = password

            if user_have:
                abort(400, msg="duplicate user")

            if not user.save():
                abort(400, msg="insert not success")

            token = generator_admin_user_token()
            cache.set(token, user.id, 60 * 60 * 24 * 100)

            data = {
                "status": HTTP_CREATE_OK,
                "msg": "insert success",
                "data": user,
                "token":token
            }
            return marshal(data,single_user_fields)
        elif action == USER_ACTION_LOGIN:
            user = get_admin_user(username)
            print(user)

            if not user:
                abort(400, msg="该用户不存在")

            if not user.check_password(password):
                abort(401, msg="用户名或密码错误，请重新输入")

            if user.is_delete:
                abort(401, msg="用户不存在")

            token = generator_admin_user_token()

            cache.set(token, user.id, 60 * 60 * 24 * 100)

            data = {
                "status": HTTP_OK,
                "msg": "login success%s" %username,
                "token": token
            }
            return data
        else:
            abort(400, msg="请提供正确参数")

