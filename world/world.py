from world.location import Location
import json

class World:
    def __init__(self):
        self.__locations: list[Location] = []
        self.__current_location = None
        self.__locations_file = "strings/locations.json"
        self.read_locations(self.__locations_file)

    def read_locations(self, file):
        with open(file, encoding='utf-8') as json_file:
            json_content = json_file.read()
        parsed_json = json.loads(json_content)
        self.parse_locations(parsed_json['locations'])

    def parse_locations(self, locations_json):
        for loc in locations_json:
            location = Location(loc['id'], loc['name'])
            nearest_locations = []
            for near_loc_id in loc['nearest_locations']:
                nearest_locations.append(near_loc_id)
            location.nearest_locations = nearest_locations
            self.__locations.append(location)

    @property
    def current_location(self):
        return  self.__current_location
