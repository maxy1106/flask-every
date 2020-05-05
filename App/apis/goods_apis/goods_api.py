import parser
from flask import request, jsonify
from flask_restful import Resource, abort, fields, marshal, marshal_with, reqparse
from App.modeles import Goods


goods_fields ={
    "id":fields.Integer,
    "name":fields.String(attribute="goods_name"),
    "goods_price":fields.Float()
}

goods_single_fields = {
    "msg" : fields.String(),
    "status":fields.Integer,
    "data":fields.Nested(goods_fields),
    "haha":fields.String
}

goods_multi_fields = {
    "msg":fields.String,
    "status":fields.Integer,
    "data":fields.List(fields.Nested(goods_fields)),
    "desc":fields.String(default="lalallalal")
}

parser = reqparse.RequestParser()
parser.add_argument("goods_name",type=str,required=True,help="please input g_name")
parser.add_argument("goods_price",type=float)
parser.add_argument("mm",action="append")

class GoodsListResource(Resource):
    @marshal_with(goods_multi_fields)
    def get(self):

        goods_list = Goods.query.all()

        data={
            "msg":"获取商品列表成功",
            "status":200,
            "data":goods_list,
            "desc":"hhe"
        }

        return data

    @marshal_with(goods_single_fields)
    def post(self):

        g_name = request.form.get("goods_name")
        g_price = request.form.get("goods_price")
        print(g_price)
        goods = Goods()
        # goods.goods_name = g_name
        # goods.goods_price = g_price
        args = parser.parse_args()
        goods.goods_name = args.get("goods_name")
        goods.goods_price = args.get("goods_price")

        print(args.get("mm"))
        if not goods.save():
            abort(404)

        data = {
            "msg":"创建成功",
            "status":200,
            "data":goods,
            "haha":"mmm"
        }
        return data

class GoodsResource(Resource):

    @marshal_with(goods_single_fields)
    def get(self,id):

        goods = Goods.query.get(id)

        data = {
            "msg":"get ok",
            "status":200,
            "data":goods,

        }

        return data

    def delete(self,id):

        goods = Goods.query.get(id)

        if not goods:
            abort(404)
        if not goods.delete():
            abort(400)

        data = {
            "msg":"delete ok",
            "status":204,
        }

        return data

    @marshal_with(goods_single_fields)
    def put(self,id):
        goods = Goods.query.get(id)

        if not goods:
            abort(404,message="goods dosn't exit")

        g_price = request.form.get("goods_price")
        g_name  = request.form.get("goods_name")

        goods.goods_name = g_name
        goods.goods_price = g_price

        if not goods.save():
            abort(400)

        data = {
            "msg" : "update ok",
            "status":203,
            "data":goods
        }

        return data

    @marshal_with(goods_single_fields)
    def patch(self,id):

        goods = Goods.query.get(id)

        if not goods:
            abort(404)

        g_price = request.form.get("goods_price")
        g_name = request.form.get("goods_name")

        goods.goods_name = g_name or goods.goods_name
        goods.goods_price = g_price or goods.goods_price

        if not goods.save():
            abort(400)

        data = {
            "msg": "update ok",
            "status": 203,
            "data": goods
        }

        return data