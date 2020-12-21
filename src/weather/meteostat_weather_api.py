# Import Meteostat library and dependencies
from datetime import datetime
from meteostat import Stations, Hourly

""" In this file we have all the connections to Meteostat, to decouple it from the rest of the code"""


def get_nearest_station(latitude: float, longitude: float) -> str:
    # Get closest weather station to the match location
    stations = Stations()
    stations = stations.nearby(latitude, longitude)
    return stations.fetch(1).index.array[0]


def get_weather(station: str, start: datetime, end: datetime) -> dict:
    # Get hourly data
    hourly_obs = Hourly(station, start, end)
    df = hourly_obs.fetch()
    return {
        "rain": df["prcp"].sum(),
        "temperature": df["temp"].mean(),
        "wind_speed": df["wspd"].mean(),
    }
