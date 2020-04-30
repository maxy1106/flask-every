from flask_restful import Api

from App.apis.movie_user_apis.movie_hall_api import UserMovieHallResource, UserMoviesHallResource
from App.apis.movie_user_apis.user_api import MovieUsersResource,MovieUserResource
from App.apis.movie_user_apis.user_order_api import MovieUserOrderResource, MovieUserOrdersResource

user_api = Api(prefix='/user')
user_api.add_resource(MovieUsersResource,'/users/')
user_api.add_resource(MovieUserResource,"/user/<int:id>")

user_api.add_resource(MovieUserOrderResource,'/order/')
user_api.add_resource(MovieUserOrdersResource,'/order/<int:orderid>')
user_api.add_resource(UserMoviesHallResource,'/hallmovies/')
user_api.add_resource(UserMovieHallResource,'/hallmovies/<int:id>/')
