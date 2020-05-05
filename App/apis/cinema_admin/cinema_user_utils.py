from flask_restful import abort

from App.ext import cache
from App.modeles.cinema_admin.movie_admin_user import CinemaAdminUser


def get_cinema_user(user_ident):

    if not user_ident:
        return None
    #根据id查找
    user = CinemaAdminUser.query.get(user_ident)
    if user:
        return user

    #根据phone 找
    user = CinemaAdminUser.query.filter(CinemaAdminUser.phone.__eq__(user_ident)).first()
    if user:
        return user

    #根据username
    user = CinemaAdminUser.query.filter(CinemaAdminUser.username.__eq__(user_ident)).first()
    if user:
        return user

    #查不到
    return None

def check_token(token):
    user_id = cache.get(token)
    user = get_cinema_user(user_id)
    if not user:
        abort(400,msg = "请登录")

    return True