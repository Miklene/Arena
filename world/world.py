from components.components_enum import ComponentsEnum
from components.inventory_component import InventoryComponent
from components.stats_component import FighterStatsComponent
from screens.equipment import EquipmentType, Weapon
from stats_requirements import WeaponStatsRequirmentsComponent
from world.location import Location
import json

from world.npc import Npc

class World:
    def __init__(self):
        self.__locations: dict[str, Location] = {}
        self.__persons: dict[str, Npc] = {}
        self.__current_location: Location = None
        self.__locations_file = "strings/locations.json"
        self.__persons_file = "strings/persons.json"
        self.read_persons(self.__persons_file)
        self.read_locations(self.__locations_file)

    def get_json_file_content(self, file, root):
        with open(file, encoding='utf-8') as json_file:
            json_content = json_file.read()
        parsed_json = json.loads(json_content)
        return parsed_json[root]

    def read_persons(self, file):
        with open(file, encoding='utf-8') as json_file:
            json_content = json_file.read()
        parsed_json = json.loads(json_content)
        self.parse_persons(parsed_json['persons'])

    def read_locations(self, file):
        with open(file, encoding='utf-8') as json_file:
            json_content = json_file.read()
        parsed_json = json.loads(json_content)
        self.parse_locations(parsed_json['locations'])

    def parse_persons(self, persons_json):
        for pers_json in persons_json:
            stats: FighterStatsComponent = FighterStatsComponent(pers_json['physique'], pers_json['strength'], pers_json['agility'])
            npc = Npc(pers_json['id'], pers_json['name'], stats)
            npc.current_dialog_id = pers_json['start_dialog']
            if 'inventory' in pers_json:
                inventory: InventoryComponent = npc.getComponent(ComponentsEnum.INVENTORY)
                for equipment in pers_json['inventory']:
                    equipment = self.get_json_file_content(equipment['file'], 'equipment')
                    for item in equipment:
                        if item['type'] == EquipmentType.WEAPON.value[0]:
                            equipment = Weapon(item['id'], item['name'], item['price'], item['damage'], WeaponStatsRequirmentsComponent(item['strength'], item['agility']))
                            inventory.addEquipment(equipment)
            self.__persons[pers_json['id']] = npc

    def parse_locations(self, locations_json):
        for loc_json in locations_json:
            location = Location(loc_json['id'], loc_json['name'])
            self.__locations[loc_json['id']] = location
        for loc_json in locations_json:
            nearest_locations = []
            for near_loc_id in loc_json['nearest_locations']:
                nearest_locations.append(self.__locations[near_loc_id])
            self.__locations[loc_json['id']].nearest_locations = nearest_locations
            persons = []
            for persons_id in loc_json['persons']:
                persons.append(self.__persons[persons_id])
            self.__locations[loc_json['id']].persons = persons

    @property
    def current_location(self) -> Location:
        return  self.__current_location

    @current_location.setter
    def current_location(self, id):
        for key, value in self.__locations.items():
            if key == id:
                self.__current_location = value
                break
