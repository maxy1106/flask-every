from flask import g
from flask_restful import Resource, reqparse, abort, fields, marshal

from App.apis.api_constant import HTTP_OK
from App.apis.cinema_admin.utils import login_required, check_user_cinema
from App.modeles.cinema_admin.cinema_address_model import CinemaAddress
from App.modeles.cinema_admin.cinema_hall_model import Hall
from App.modeles.cinema_admin.cinema_movie_model import CinemaMovie
from App.modeles.cinema_admin.hall_movie_model import HallMovie
from App.modeles.common.movie_model import Movie

parse = reqparse.RequestParser()
parse.add_argument("movie_id",type=int,required=True,help="请选择电影")
parse.add_argument("hall_id",type=int,required=True,help="请选择影厅")
parse.add_argument("h_time",required=True,help="请选择播放时间")

hall_movie_fields = {
    "h_id":fields.Integer,
    "m_id":fields.Integer,
    "h_m_date":fields.DateTime
}

class HallMoviesResource(Resource):
    def get(self):
        hall_movie = HallMovie()
        return {"msg":"ok"}

    @login_required
    def post(self):
        args = parse.parse_args()
        movie_id = args.get("movie_id")
        hall_id = args.get("hall_id")
        h_time = args.get("h_time")

        """
        验证 
        1.hall id 是否是登录用户影院的
        2.movie 是否是已经购买
        3.所选时间是否比当前时间提前一天，并在14天之内
        4.所选时间该 hall 是否有排挡
        """
        cinema_user = g.user

        cinema_list = CinemaAddress.query.filter(CinemaAddress.c_user == cinema_user.id).all()

        """
        cinema 表 和 
        """

        hall_list=[]
        movie_list=[]
        print(cinema_list)
        for cinema in cinema_list:
            cinema_hall_list = Hall.query.filter(Hall.h_address_id == cinema.id).all()
            cinema_movie_list = CinemaMovie.query.filter(CinemaMovie.c_cinema_id == cinema.id).all()
            print(cinema_movie_list)
            for cinema_hall in cinema_hall_list:
                hall_list.append(cinema_hall)

            for cinema_movie in cinema_movie_list:
                movie_list.append(cinema_movie)

        hall_list_ids = [hall.id for hall in hall_list]
        movie_list_ids = [movie.c_movie_id for movie in movie_list]
        print(movie_list_ids)

        if not hall_id in hall_list_ids:
            abort(403,msg="没有权限操作该hall")

        if not movie_id in movie_list_ids:
            abort(403,msg="没有权限操作该电影")

        hall_movie = HallMovie()
        hall_movie.h_id = hall_id
        hall_movie.m_id = movie_id
        hall_movie.h_m_date = h_time

        if not hall_movie.save():
            abort(400,msg = "存储排档失败")

        data = {
            "msg":"create hall_movie success",
            "status":HTTP_OK,
            "data":marshal(hall_movie,hall_movie_fields)
        }

        return data