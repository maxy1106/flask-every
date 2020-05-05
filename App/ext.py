from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_caching import Cache

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
cache = Cache(
    config={
        "CACHE_TYPE": "redis",
        'CACHE_REDIS_HOST': '123.57.148.207',
        'CACHE_REDIS_PORT': 6379,
        'CACHE_KEY_PREFIX':''
    }
)


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    cache.init_app(app)
