from entities.creature import Creature


class Location:
    def __init__(self, id: str, name: str):
        self.__id = id
        self.__name = name
        self.__persons: list[Creature] = []
        self.__nearest_locations: list[Location] = []

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def nearest_locations(self):
        return self.__nearest_locations

    @property
    def persons(self):
        return self.__persons

    @nearest_locations.setter
    def nearest_locations(self, locations):
        self.__nearest_locations = locations
