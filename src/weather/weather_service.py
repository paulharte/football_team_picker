from datetime import datetime

from src.weather.match_weather import MatchWeather
from src.weather.meteostat_weather_api import get_nearest_station, get_weather
from src.weather.weather_cache import WeatherCache


class WeatherService(object):
    def __init__(self, latitude: float, longitude: float):
        self.station = get_nearest_station(latitude, longitude)
        self.cache = WeatherCache()

    def set_station(self, station_id: str):
        """ Used to override the default station, in case of a duff one, i.e. casement aerodrome """
        try:
            int(station_id)
        except ValueError:
            raise RuntimeError('Station Ids must be numeric: %s' % station_id)
        self.station = station_id

    def get_weather(self, start: datetime, end: datetime) -> MatchWeather:
        if self.cache.get(start, end):
            return self.cache.get(start, end)
        weather_dict = get_weather(self.station, start, end)
        out = MatchWeather(weather_dict, start, end)
        self.cache.set(out)
        return out
