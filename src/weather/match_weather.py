class MatchWeather(object):
    """ This class represents the weather conditions during a single match """

    temperature: float
    rain: float
    wind_speed: float

    def __init__(self, weather_dict: dict):
        self.temperature = weather_dict.get("temperature")
        self.rain = weather_dict.get("rain")
        self.wind_speed = weather_dict.get("wind_speed")

    def __str__(self):
        return "Weather: temperature %.2f degrees C, rain %.2f mm, wind %.2f kph" % (
            self.temperature,
            self.rain,
            self.wind_speed,
        )
