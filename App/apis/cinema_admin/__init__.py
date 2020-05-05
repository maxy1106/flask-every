from flask_restful import Api

from App.apis.cinema_admin.cinema_address_api import CinemaAddressesResource, CinemaAddressResource
from App.apis.cinema_admin.cinema_hall_api import CinemaHallsResource
from App.apis.cinema_admin.cinema_hall_movie_api import HallMoviesResource
from App.apis.cinema_admin.cinema_movie_api import CinemaMoviesResource
from App.apis.cinema_admin.cinema_user_api import CinemaUserResource, CinemaUsersResource

cinema_api = Api(prefix='/cinema')

cinema_api.add_resource(CinemaUserResource,'/users/<int:id>')
cinema_api.add_resource(CinemaUsersResource,'/users/')
cinema_api.add_resource(CinemaAddressesResource,'/addresses/')
cinema_api.add_resource(CinemaAddressResource,'/addresses/<int:id>/')
cinema_api.add_resource(CinemaMoviesResource,'/cinemamovies/')
cinema_api.add_resource(CinemaHallsResource,'/cinemahalls/')
cinema_api.add_resource(HallMoviesResource,'/hallmovies/')