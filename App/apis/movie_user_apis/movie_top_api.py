from flask_restful import Resource, fields, marshal
from sqlalchemy import func

from App.apis.api_constant import HTTP_OK
from App.ext import db
from App.modeles.cinema_admin.hall_movie_model import HallMovie
from App.modeles.common.movie_model import Movie
from App.modeles.user import MovieUser
from App.modeles.user.movie_order_model import MovieOrder

top_fileds = {
    "id":fields.Integer,
    "showname":fields.String,
    "o_price":fields.Float
}

class MovieTopResource(Resource):
    def get(self):

        result_list = []

        results = db.session.query(Movie.id,Movie.showname,func.sum(MovieOrder.o_price)).join(Movie.hall_movies).join(HallMovie.o_movie_orders).group_by(Movie.id).order_by(-func.sum(MovieOrder.o_price))

        for result in results:
            result_list.append(result)

        print(result_list)

        data = {
            "msg":"ok",
            "status":HTTP_OK,
            "data":marshal(result_list,top_fileds)
        }


        return data