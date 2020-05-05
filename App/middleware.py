from flask import request,g
def load_middleware(app):
    @app.before_request
    def before():
        g.msg = "呵呵呵"
        print("中间件",request.url)
        """
        统计
        反爬
        优先级
        用户认证
        用户权限
        """

    # @app.after_app_request
    # def after(response):
    #     print("after", response)
    #     print(type(response))
    #     return response