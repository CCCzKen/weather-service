from flask import Blueprint
from webargs import fields
from webargs.flaskparser import use_kwargs

from src.utils.jsonify import JsonpResp

from src.utils.stack import Stack


bp = Blueprint('api', __name__)


@bp.route('/weather/search')
@use_kwargs(
    {
        "city": fields.Str(missing=''),
    },
    location="querystring"
)
def get_weather_search(city):
    """
    查询天气接口
    ---
    parameters:
      - name: city
        required: true
        default: GuangZhou
    definitions:
      Response:
        type: object
        properties:
          city:
            type: string
            description: 城市
          temperature:
            type: string
            description: 温度
          descriptions:
            type: string
            description: 天气
    responses:
      200:
        description: 返回城市天气
        schema:
          $ref: '#/definitions/Response'
        examples:
          rgb: ['red', 'green', 'blue']
    """
    weather_api = Stack()
    data = weather_api.get_city_weather(city)
    return JsonpResp.success(data=data)
