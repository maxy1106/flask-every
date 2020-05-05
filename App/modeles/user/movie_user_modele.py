from flask_restful import fields
from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import db
from App.modeles import BaseModel
from App.modeles.user.model_constant import COMMON_USER, BLACK_USER


class MovieUser(BaseModel):

    username = db.Column(db.String(32),unique=True)
    _password = db.Column(db.String(256))
    phone = db.Column(db.String(32),unique=True)
    is_delete = db.Column(db.Boolean,default=False)
    permission = db.Column(db.Integer,default=COMMON_USER)


    @property
    def password(self):
        raise Exception("password con't access")

    @password.setter
    def password(self,password_value):
        self._password = generate_password_hash(password_value)

    def check_password(self,password_value):
        return check_password_hash(self._password,password_value)

    def check_permission(self,permission):
        if (BLACK_USER & permission) == BLACK_USER:
            return False
        elif self.permission & permission == permission:
            return True
