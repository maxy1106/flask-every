from flask import g
from flask_restful import Resource, reqparse, abort, fields, marshal

from App.apis.api_constant import HTTP_OK
from App.apis.cinema_admin.utils import login_required
from App.modeles.cinema_admin.cinema_movie_model import CinemaMovie
from App.modeles.common.movie_model import Movie

parse = reqparse.RequestParser()
parse.add_argument("movieId",type=int,required=True,help="请输入movieID")

movie_fields = {
    "id":fields.Integer,
    "showname":fields.String,
    "shownameen":fields.String,
    "director":fields.String,
    "leadingrole":fields.String,
    "type":fields.String,
    "country":fields.String,
    "language":fields.String,
    "duration":fields.String,
    "screeningmodel":fields.String,
    "openday":fields.String,
    "backgroundpicture":fields.String,
}
mulit_movie_fields = {
    "msg":fields.String,
    "status":fields.Integer,
    "data":fields.List(fields.Nested(movie_fields))
}

class CinemaMoviesResource(Resource):

    @login_required
    def get(self):
        user_id = g.user.id
        cinema_movies = CinemaMovie.query.filter(CinemaMovie.c_cinema_id == user_id).all()
        movies = []
        for cinema_movie in cinema_movies:
            movies.append(Movie.query.get(cinema_movie.c_movie_id))

        data = {
            "msg":"get movies success",
            "status":HTTP_OK,
            "data":movies
        }
        return marshal(data,mulit_movie_fields)

    @login_required
    def post(self):
        user_id = g.user.id
        args = parse.parse_args()
        movie_id = args.get("movieId")

        movie = Movie.query.get(movie_id)

        if not movie:
            abort(403,msg = "该电影不存在，请重新选择")

        cinema_movies = CinemaMovie.query.filter(CinemaMovie.c_cinema_id==user_id).filter(CinemaMovie.c_movie_id == movie_id).all()

        if cinema_movies:
            abort(400,msg = "该电影已经购买")

        cinema_movie = CinemaMovie()
        cinema_movie.c_movie_id = movie_id
        cinema_movie.c_cinema_id = user_id

        if not cinema_movie.save():
            abort(400,msg = "电影购买失败")

        data = {
            "msg":"buy movie success",
            "status":HTTP_OK,
        }

        return data

