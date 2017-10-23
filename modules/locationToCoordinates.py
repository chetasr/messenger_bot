# Import essentials

import geopy.geocoders

# Definitions

class locationToCoordinates:
    # To get coordinates of a location string
    def __init__(self):
        self.inp = 'location'
        self.out = 'coords'

    def do(self, entities):
        loc = geopy.geocoders.Nominatim()
        entities['coords'] = loc.geocode(entities['location'])
        return entities
