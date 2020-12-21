from datetime import datetime
from unittest import TestCase, mock

from src.weather import weather_service


class TestWeatherService(TestCase):
    def test_get_weather(self):
        weather_service.get_nearest_station = mock.Mock(return_value="Dublin")
        weather_service.get_weather = mock.Mock(
            return_value={"rain": 1.1, "temperature": 10.0}
        )

        # Set coordinates of Dublin
        lat = 53.3067
        lon = -6.2210
        serv = weather_service.WeatherService(lat, lon)
        start = datetime(2020, 12, 14, 21, 00)
        end = datetime(2020, 12, 14, 22, 00)
        conditions = serv.get_weather(start, end)
        self.assertEqual(conditions.temperature, 10.0)
        self.assertEqual(conditions.rain, 1.1)
        self.assertEqual(conditions.wind_speed, None)
