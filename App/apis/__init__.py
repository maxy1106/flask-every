from App.apis.admin_apis import admin_api
from App.apis.cinema_admin import cinema_api
from App.apis.common import common_api
from App.apis.goods_apis import goods_api
from App.apis.movie_user_apis import user_api


def init_api(app):
    goods_api.init_app(app)
    user_api.init_app(app)
    common_api.init_app(app)
    admin_api.init_app(app)
    cinema_api.init_app(app)




