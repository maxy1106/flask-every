from App.ext import db
from App.modeles import BaseModel
from App.modeles.cinema_admin.hall_movie_model import HallMovie

ORDER_STATUS_NOT_PAY = 0
ORDER_STATUS_PAYED_NOT_GET = 1
ORDER_STATUS_GET = 2
ORDER_STATUS_TIMEOUT = 3



class MovieOrder(BaseModel):
    # o_user_id = db.Column(db.Integer,db.ForeignKey(MovieUser.id))
    o_user_id = db.Column(db.Integer,db.ForeignKey("movie_user.id"))# 表名+字段 防止循环导入
    o_hall_movie_id = db.Column(db.Integer,db.ForeignKey(HallMovie.id))
    o_time = db.Column(db.DateTime)
    o_status = db.Column(db.Integer,default=ORDER_STATUS_NOT_PAY)
    o_seats = db.Column(db.String(256))
    o_price = db.Column(db.Float,default=0)
