
from flask_restful import Resource, fields, marshal

from App.apis.api_constant import HTTP_OK
from App.modeles.common import CityModel, Letter

cities_fileds = {
    "id":fields.Integer(attribute="c_id"),
    "parentId":fields.Integer(attribute="c_parent_id"),
    "regionName":fields.String(attribute="c_region_name"),
    "cityCode":fields.Integer(attribute="c_city_code"),
    "pinYin":fields.String(attribute="c_pinyin")
}


class CitiesResource(Resource):
    def get(self):
        """
        返回城市接口
        :return:
        msg
        status
        data
        """

        letter_list = Letter.query.all()

        letter_cities = {}
        letter_fields = {}

        for letter in letter_list:
            cities_list = CityModel.query.filter_by(letter_id = letter.id)
            letter_cities[letter.letter] = cities_list
            letter_fields[letter.letter] = fields.List(fields.Nested(cities_fileds))

        data = {
            "msg":"city list",
            "status":HTTP_OK,
            "data":marshal(letter_cities,letter_fields)
        }
        return data