from flask_restful import Resource, reqparse, fields, marshal

from App.apis.api_constant import HTTP_OK
from App.apis.movie_user_apis.utils import login_required
from App.modeles.cinema_admin.cinema_hall_model import Hall
from App.modeles.cinema_admin.hall_movie_model import HallMovie

parse = reqparse.RequestParser()
parse.add_argument("address_id")
parse.add_argument("district")
parse.add_argument("movie_id")




hall_movie_fields = {
    "id":fields.Integer,
    "h_id":fields.Integer,
    "m_id":fields.Integer,
    "h_m_date":fields.DateTime
}

mutil_hall_movie_fields = {
    "msg":fields.String,
    "status":fields.Integer,
    "data":fields.List(fields.Nested(hall_movie_fields))
}
class UserMoviesHallResource(Resource):
    def get(self):
        args = parse.parse_args()
        address_id = args.get("address_id")
        district = args.get("district")
        movie_id = args.get("movie_id")

        halls = Hall.query.filter(Hall.h_address_id==address_id).all()

        hall_movies = []

        print(halls)

        for hall in halls:
            hall_movie = HallMovie.query.filter(HallMovie.h_id == hall.id).filter(HallMovie.m_id==movie_id).all()
            hall_movies += hall_movie
        print(hall_movies)

        data = {
            "msg":"get success",
            "status":HTTP_OK,
            "data":hall_movies
        }

        return marshal(data,mutil_hall_movie_fields)

hall_fields = {
    "id":fields.Integer,
    "h_address_id":fields.Integer,
    "h_num":fields.String,
    "h_seate":fields.String
}

class UserMovieHallResource(Resource):
    """
    单个排挡下单
    """
    @login_required
    def get(self,id):
        hall_movie = HallMovie.query.get(id)
        print(id)

        hall = Hall.query.get(hall_movie.h_id)

        data = {
            "msg":"hall info ok",
            "status":HTTP_OK,
            "data":marshal(hall,hall_fields)
        }

        return data