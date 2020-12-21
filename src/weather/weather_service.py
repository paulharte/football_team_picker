from datetime import datetime

from src.weather.match_weather import MatchWeather
from src.weather.meteostat_weather_api import get_nearest_station, get_weather


class WeatherService(object):
    def __init__(self, latitude: float, longitude: float):
        self.station = get_nearest_station(latitude, longitude)

    def get_weather(self, start: datetime, end: datetime) -> MatchWeather:
        # TODO: put some caching in here to speed things up
        weather_dict = get_weather(self.station, start, end)
        return MatchWeather(weather_dict)
