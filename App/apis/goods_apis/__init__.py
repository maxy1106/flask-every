from flask_restful import Api

from App.apis.goods_apis.goods_api import GoodsListResource,GoodsResource

goods_api = Api(prefix="/good")


goods_api.add_resource(GoodsListResource,"/goods/")
goods_api.add_resource(GoodsResource,"/goods/<int:id>")