import pymysql
import os


def geturi(datainfo):
    enging = datainfo.get('ENGING')
    driver = datainfo.get('DRIVER')
    username = datainfo.get('USERNAME')
    password = datainfo.get('PASSWORD')
    host = datainfo.get('HOST')
    port = datainfo.get('PORT')
    name = datainfo.get('NAME')
    return "{}+{}://{}:{}@{}:{}/{}".format(enging,driver,username,password,host,port,name)



class Config():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "SBFOIWEBGlasdnapefwbepNSFLWFWE"

    MAIL_SERVER = "smtp.163.com"
    MAIL_PORT = 25
    MAIL_USERNAME = "m15600352552@163.com"
    MAIL_PASSWORD = 'OPLGRDPOJYXPNNBL'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

class DevelopConnection(Config):
    DEBUG = True
    datainfo={
        'ENGING':'mysql',
        'DRIVER':'pymysql',
        'USERNAME':'root',
        'PASSWORD':'root',
        'HOST':'123.57.148.207',
        'PORT':'3306',
        'NAME':'flaskTpp'
    }
    SQLALCHEMY_DATABASE_URI = geturi(datainfo)

class TestingConnection(Config):
    datainfo={
        'ENGING':'mysql',
        'DRIVER':'pymysql',
        'USERNAME':'root',
        'PASSWORD':'root',
        'HOST':'123.57.148.207',
        'PORT':'3306',
        'NAME':'flaskAPI'
    }
    SQLALCHEMY_DATABASE_URI = geturi(datainfo)


envs = {
    'develop' :DevelopConnection,
    'testing' :TestingConnection
}

BASE_DIR = os.path.dirname(__file__)
FILE_UP_LOADS = '/static/movie/icon/'
FILE_UP_LOADS_PATH = BASE_DIR + '/static/movie/icon/'

#支付宝
ALIPAY_APPID="2016102300744109"
APP_PRIVATE_KEY = open(os.path.join(BASE_DIR,"alipay_config/app_private_2048.pem"),'r').read()
ALIPAY_PUBLIC_KEY = open(os.path.join(BASE_DIR,"alipay_config/alipay_public_2048.pem"),'r').read()