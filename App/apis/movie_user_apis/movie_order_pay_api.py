from alipay import AliPay, DCAliPay, ISVAliPay
from flask_restful import Resource, marshal, fields

from App.apis.api_constant import HTTP_OK
from App.apis.movie_user_apis.utils import login_required
from App.modeles.user.movie_order_model import MovieOrder
from App.setting import ALIPAY_APPID, ALIPAY_PUBLIC_KEY, APP_PRIVATE_KEY

movie_order_fields = {
    "o_price":fields.Float,
    "o_seats":fields.String,
    "o_hall_movie_id":fields.Integer,
    "o_status":fields.String,
    "o_user_id":fields.Integer
}

class MovieOrderPayResource(Resource):

    @login_required
    def get(self,id):

        movie_order = MovieOrder.query.get(id)
        alipay_client = AliPay(
            appid=ALIPAY_APPID,
            app_notify_url=None,  # 默认回调url
            app_private_key_string=APP_PRIVATE_KEY,
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            alipay_public_key_string=ALIPAY_PUBLIC_KEY,
            sign_type="RSA2", # RSA 或者 RSA2
            debug=False  # 默认False
        )

        subject = "buy phone"

        order_string = alipay_client.api_alipay_trade_page_pay(
            out_trade_no=id,
            total_amount=movie_order.o_price,
            subject=subject,
            return_url="http://www.1000phone.com",#服务器对外暴露的地址，回调地址
            notify_url="http://www.1000phone.com"

        )
        pay_url = "https://openapi.alipaydev.com/gateway.do?" + order_string

        data = {
            "msg":"pay ok",
            "status":HTTP_OK,
            "data":{
                "pay_url":pay_url,
                "order_string": order_string,
                "order_info":marshal(movie_order,movie_order_fields)
            }
        }

        return data




        # dc_alipay = DCAliPay(
        #     appid="appid",
        #     app_notify_url="http://example.com/app_notify_url",
        #     app_private_key_string=app_private_key_string,
        #     app_public_key_cert_string=app_public_key_cert_string,
        #     alipay_public_key_cert_string=alipay_public_key_cert_string,
        #     alipay_root_cert_string=alipay_root_cert_string
        # )

        # 如果您没有听说过ISV， 那么以下部分不用看了
        # app_auth_code或app_auth_token二者需要填入一个
        # isv_alipay = ISVAliPay(
        #     appid="",
        #     app_notify_url=None,  # 默认回调url
        #     app_private_key_srting="",
        #     # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        #     alipay_public_key_string="",
        #     sign_type="RSA" # RSA or RSA2
        #     debug=False  # False by default,
        #     app_auth_code=None,
        #     app_auth_token=None
        # )