
from flask_restful import Resource, reqparse, abort, fields, marshal
from werkzeug.datastructures import FileStorage

from App.apis.admin_apis.utils import login_required
from App.apis.api_constant import HTTP_OK
from App.apis.common.utils import transfor_file
from App.modeles.common.movie_model import Movie

parse = reqparse.RequestParser()
parse.add_argument("token", required=True, help="请输入token")
parse.add_argument("showname", required=True, help="请输入电影名")
parse.add_argument("shownameen", required=True, help="请输入电影英文名")
parse.add_argument("director", required=True, help="请输入导演")
parse.add_argument("leadingrole", required=True, help="请输入主演")
parse.add_argument("type", required=True, help="请输入电影类型")
parse.add_argument("country", required=True, help="请输入电影国家")
parse.add_argument("language", required=True, help="请输入电影语言")
parse.add_argument("duration", type=int, required=True, help="请输入电影时长")
parse.add_argument("screeningmodel", required=True, help="请输入电影荧屏")
parse.add_argument("openday", required=True, help="请输入电影上线时间")
parse.add_argument("backgroundpicture",type = FileStorage,required=True, help="请输入电影背景图",location = 'files')#

movie_fields = {
    "showname":fields.String,
    "shownameen":fields.String,
    "director":fields.String,
    "leadingrole":fields.String,
    "type":fields.String,
    "country":fields.String,
    "language":fields.String,
    "duration":fields.String,
    "screeningmodel":fields.String,
    "openday":fields.String,
    "backgroundpicture":fields.String,
}
mulit_movie_fields = {
    "msg":fields.String,
    "status":fields.Integer,
    "data":fields.List(fields.Nested(movie_fields))
}

class MovieResource(Resource):
    def get(self):
        movie = Movie.query.all()
        data = {
            "msg":"query success",
            "status":HTTP_OK,
            "data":movie
        }
        return marshal(data,mulit_movie_fields)

    @login_required
    def post(self):
        args = parse.parse_args()
        showname = args.get("showname")
        shownameen = args.get("shownameen")
        director = args.get("director")
        leadingrole = args.get("leadingrole")
        _type = args.get("type")
        country = args.get("country")
        langusge = args.get("language")
        duration = args.get("duration")
        screeningmodel = args.get("screeningmodel")
        openday = args.get("openday")
        # backgroundpicture = request.files.get("backgroundpicture")
        backgroundpicture = args.get("backgroundpicture")
        print(type(backgroundpicture))

        movie = Movie()
        movie.showname = showname
        movie.shownameen = shownameen
        movie.director = director
        movie.leadingRole = leadingrole
        movie.type = _type
        movie.country = country
        movie.language = langusge
        movie.duration = duration
        movie.screeningmodel = screeningmodel
        movie.openday = openday

        result = transfor_file(backgroundpicture)

        movie.backgroundpicture = result[1]

        if not movie.save():
            abort(403,msg = "存储失败")

        data = {
            "msg":"create movie success",
            "status": HTTP_OK,
            "data":marshal(movie,movie_fields)
        }
        return data

class MoviesResource(Resource):

    def get(self,id):
        print(id)
        movie = Movie.query.get(id)
        if not movie:
            abort(404,msg = "movie not exist")

        data = {
            "msg":"get movie success",
            "status":HTTP_OK,
            "data":marshal(movie,movie_fields)
        }
        return data


