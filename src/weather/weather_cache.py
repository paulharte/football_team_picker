from datetime import datetime

from src.weather.match_weather import MatchWeather


class WeatherCache(object):
    def __init__(self):
        self._cache = {}

    def get(self, start: datetime, end: datetime) -> MatchWeather:
        key = _form_key(start, end)
        return self._cache.get(key)

    def set(self, weather: MatchWeather):
        key = _form_key(weather.start, weather.end)
        self._cache[key] = weather


def _form_key(start: datetime, end: datetime) -> str:
    return str(start) + str(end)