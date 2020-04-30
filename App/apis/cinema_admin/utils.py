from flask import request, g
from flask_restful import abort

from App.apis.cinema_admin.cinema_user_utils import get_cinema_user
from App.apis.utils import CINEMAUSER
from App.ext import cache


#私有函数
from App.modeles.cinema_admin.cinema_address_model import CinemaAddress


def _verify():
    token = request.args.get("token")
    if not token:
        abort(401, msg="请输入有效认证")

    if not token.startswith(CINEMAUSER):
        abort(403,msg="登录信息错误")
    user_id = cache.get(token)
    if not user_id:
        abort(401, msg="验证已过期，请登录")

    user = get_cinema_user(user_id)
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

        def wrapper(*args,**kwargs):

            _verify()

            if not g.user.check_permission(permission):
                abort(403,msg = "user can't access")
            return func(*args, **kwargs)
        return wrapper
    return required_permmsion_wrapper


def check_user_cinema(cinema_user,address_id):
    cinemas = CinemaAddress.query.filter(CinemaAddress.c_user == cinema_user.id).all()

    for cinema in cinemas:
        if cinema.id == address_id:
            return True
    return None







