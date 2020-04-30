from App.ext import db
from App.modeles import BaseModel
from App.modeles.cinema_admin.movie_admin_user import CinemaAdminUser
from App.modeles.common.movie_model import Movie


class CinemaMovie(BaseModel):
    c_cinema_id = db.Column(db.Integer,db.ForeignKey(CinemaAdminUser.id))
    c_movie_id = db.Column(db.Integer,db.ForeignKey(Movie.id))
