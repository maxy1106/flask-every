from App.ext import db
from App.modeles import BaseModel
from App.modeles.cinema_admin.cinema_hall_model import Hall
from App.modeles.common.movie_model import Movie


class HallMovie(BaseModel):
    h_id = db.Column(db.Integer,db.ForeignKey(Hall.id))
    m_id = db.Column(db.Integer,db.ForeignKey(Movie.id))
    h_m_date = db.Column(db.DateTime)
