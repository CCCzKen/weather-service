import requests

from flask import current_app

from src.utils.exceptions import ApiError


class Stack(object):
    """天气接口"""

    def __init__(self):
        self.access_key = current_app.config['WEATHER_ACCESS_KEY']

    def get_city_weather(self, city):
        url = "http://api.weatherstack.com/current?access_key={}&query={}".format(self.access_key, city)
        response = requests.get(url)
        data = response.json()
        location = data.get('location')
        current = data.get('current')

        if not location:
            raise ApiError('找不到该城市')

        data = {
            "city": location.get('name', ''),
            "temperature": current.get('temperature', 0),
            "descriptions": current.get('weather_descriptions', [''])[0]
        }

        return data
