from datetime import datetime
from meteostat import Stations, Hourly
import logging

""" In this file we have all the connections to Meteostat, to decouple it from the rest of the code"""

LOGGER = logging.getLogger("meteostat_weather_api")

def get_nearest_station(latitude: float, longitude: float) -> str:
    # Get closest weather station to the match location
    stations = Stations().nearby(latitude, longitude)
    station = stations.fetch(1)
    LOGGER.info("Using nearest station: %s" % station)
    return station.index.array[0]


def get_weather(station: str, start: datetime, end: datetime) -> dict:
    # Get hourly data
    hourly_obs = Hourly(station, start, end)
    df = hourly_obs.fetch()
    return {
        "rain": df["prcp"].fillna(0).sum(),
        "temperature": df["temp"].mean(),
        "wind_speed": df["wspd"].mean(),
    }
