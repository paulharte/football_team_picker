from datetime import datetime
from unittest import TestCase

from src.weather.match_weather import MatchWeather
from src.weather.weather_cache import WeatherCache


class TestWeatherCache(TestCase):
    def test_get(self):
        cache = WeatherCache()
        temp = 21.1
        start = datetime(2020, 12, 14, 21, 00)
        end = datetime(2020, 12, 14, 22, 00)
        weather = MatchWeather({"temperature": temp}, start, end)
        cache.set(weather)
        self.assertEqual(cache.get(start, end).temperature, temp )

        bad_start = datetime(1920, 12, 14, 21, 00)
        bad_end = datetime(1920, 12, 14, 22, 00)
        self.assertEqual(cache.get(bad_start, bad_end), None)