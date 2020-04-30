from flask import request, g
from flask_restful import abort

from App.apis.admin_apis.admin_user_utils import get_admin_user
from App.apis.utils import ADMINUSER
from App.ext import cache


#私有函数
def _verify():
    token = request.args.get("token")
    print(token)
    if not token:
        abort(401, msg="请输入有效认证")

    if not token.startswith(ADMINUSER):
        abort(403,msg="登录信息错误")

    user_id = cache.get(token)
    if not user_id:
        abort(401, msg="验证已过期，请登录")

    user = get_admin_user(user_id)
    if not user:
        abort(401, msg="用户信息不可用，请登录")

    g.user = user
    g.auth = token

def login_required(func):
    def wrapper(*args,**kwargs):

        _verify()

        return func(*args,**kwargs)

    return wrapper


def required_permmsion(permission):
    def required_permmsion_wrapper(func):
        print("**",func)
        def wrapper(*args,**kwargs):

            _verify()

            if not g.user.check_permission(permission):
                abort(403,msg = "user can't access")
            return func(*args, **kwargs)
        return wrapper
    return required_permmsion_wrapper







