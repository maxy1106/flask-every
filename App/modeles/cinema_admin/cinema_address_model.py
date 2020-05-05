from App.ext import db
from App.modeles import BaseModel
from App.modeles.cinema_admin.movie_admin_user import CinemaAdminUser

"""
电影院信息
"""

class CinemaAddress(BaseModel):
    c_user = db.Column(db.Integer,db.ForeignKey(CinemaAdminUser.id))
    name = db.Column(db.String(64))
    city = district = db.Column(db.String(16))
    district = db.Column(db.String(16))
    address = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    score = db.Column(db.Float,default=10)
    hallnum = db.Column(db.Integer,default=1)
    servicecharge = db.Column(db.Float,default=10)
    astrict = db.Column(db.Float,default=10)
    flag = db.Column(db.Boolean,default=False)
    is_delete = db.Column(db.Boolean,default=False)


