# Import essentials

import forecastio
import os

# Definitions


class weatherFromCoordinates:
    # Get weather of a particular coordinate
    def __init__(self):
        self.inp = 'coords'
        self.out = 'weather'

    def do(self, entities):
        forecast = forecastio.load_forecast(
            os.environ['FORECASTIO_KEY'], entities['coords'].latitude, entities['coords'].longitude)
        entities['weather'] = [forecast.hourly().summary]
        return entities
