from App.ext import db
from App.modeles import BaseModel


class Movie(BaseModel):
    __tablename__ = "movies"
    showname = db.Column(db.String(64))
    shownameen = db.Column(db.String(128))
    director = db.Column(db.String(64))
    leadingRole = db.Column(db.String(256))
    type = db.Column(db.String(64))
    country = db.Column(db.String(64))
    language = db.Column(db.String(64))
    duration = db.Column(db.Integer,default=90)
    screeningmodel = db.Column(db.String(32))
    openday = db.Column(db.DateTime)
    backgroundpicture = db.Column(db.String(256))
    flag = db.Column(db.Boolean,default=False)
    isdelete = db.Column(db.Boolean,default=False)
    hall_movies = db.relationship("HallMovie",backref = "Movie",lazy=True)