from contextlib import suppress
from components.inventory_component import InventoryComponent
from components.parameters_component import FighterParametersComponent
from components.stats_component import FighterStatsComponent, StatsComponent
from entities.creature import Creature
from PyQt5.QtGui import QColor
from mvp.game_window.game_window_view import GameWindowView
import xml.etree.ElementTree as ET
import json
from screens.equipment import Weapon
from stats_requirements import WeaponStatsRequirmentsComponent
from components.components_enum import ComponentsEnum
from world.location import Location
from world.npc import Npc
from world.world import World

class GameWindowPresenter:

    SELF_COLOR = QColor(0x0000FF)
    OPPONENT_COLOR = QColor(0x009900)
    BASIC_COLOR = QColor(0x000000)

    def __init__(self, view, player: Creature):
        self.__view: GameWindowView = view
        self.__player: Creature = player
        self.__current_message_id = 0
        self.__current_message_file = 'strings/new_game.json'

        self.__current_variatns = {}

        self.read_new_message_file()
        self.__print_message()
        self.__equipment_visible = False
        self.__stats_visible = False

        self.__world = World()
        self.set_current_location('village_saraevo')

    def read_new_message_file(self):
        with open(self.__current_message_file, encoding='utf-8') as json_file:
            json_content = json_file.read()
        parsed_json = json.loads(json_content)
        self.__messages = parsed_json['messages']

    def set_current_location(self, location_id: str):
        self.__world.current_location = location_id
        self.__view.set_locations_to_list(self.__world.current_location.nearest_locations)
        self.__view.set_persons_to_list(self.__world.current_location.persons)

    def __print_message(self):
        self.__view.clear_variants()
        self.__current_variatns.clear()
        for message in self.__messages:
            if message['id'] == self.__current_message_id:
                text = message.get('text')
                if 'author' in message:
                    self.__view.set_log_text_color(self.OPPONENT_COLOR)
                    self.__view.add_text_to_log(message['author'])
                    self.__view.set_log_text_color(self.BASIC_COLOR)
                    self.__view.insert_text_to_log(text)
                else:
                    self.__view.add_text_to_log(text)
                if 'actions' in message:
                    for action in message['actions']:
                        self.__view.add_text_to_log(action['text'])
                        if action['type'] == 'REWARD':
                            reward_file = action['file']
                            reward_id = action['id']
                            with open(reward_file, encoding='utf-8') as json_file:
                                json_content = json_file.read()
                                parsed_json = json.loads(json_content)
                                weapons = parsed_json['weapons']
                                for item in weapons:
                                    if item['id'] == reward_id:
                                        weapon_requirments = WeaponStatsRequirmentsComponent(item['strength'], item['agility'])
                                        weapon = Weapon(item['name'],item['price'], item['damage'],weapon_requirments)
                                        self.__view.insert_text_to_log(weapon.name)
                                        inventory:InventoryComponent = self.__player.getComponent(ComponentsEnum.INVENTORY)
                                        inventory.addEquipment(weapon)
                                        break
                        if action['type'] == 'STATS':
                            reward_file = action['file']
                            reward_id = action['id']
                            with open(reward_file, encoding='utf-8') as json_file:
                                json_content = json_file.read()
                                parsed_json = json.loads(json_content)
                                stats = parsed_json['stats']
                                for item in stats:
                                    if item['id'] == reward_id:
                                        text = item['name']
                                        self.__view.insert_text_to_log(text)
                                        amount = " + " + str(action['amount'])
                                        self.__view.insert_text_to_log(amount)
                                        stats: FighterStatsComponent = self.__player.getComponent(ComponentsEnum.STATS)
                                        if item['id'] == 0:
                                            stats.increasePhysique(action['amount'])
                                        if item['id'] == 1:
                                            stats.increaseStrength(action['amount'])
                                        if item['id'] == 2:
                                            stats.increaseAgility(action['amount'])
                                        break
                self.__add_variants(message)


    def __add_variants(self, message):
        variants = message['variants']
        for variant in variants:
             self.__view.add_variant(variant['text'], variant['id'])
             self.__current_variatns[variant['id']] = variant
        #for variant in message.findall('variant'):
        #    self.__view.add_variant(variant.find('text').text, int(variant.get('id')))
        #    self.__current_variatns[int(variant.get('id'))] = variant

    def button_stats_clicked(self):
        if not self.__stats_visible:
            self.__stats_visible = True
            self.__equipment_visible = False
            self.__view.hide_inventory()
            self.__view.show_stats(self.__player)
        else:
            self.__stats_visible = False
            self.__view.hide_stats()

    def button_abilities_clicked(self):
        pass

    def button_equipment_clicked(self):
        if not self.__equipment_visible:
            self.__equipment_visible = True
            self.__stats_visible = False
            self.__view.hide_stats()
            inventory:InventoryComponent = self.__player.getComponent(ComponentsEnum.INVENTORY)
            self.__view.show_inventory(inventory)
        else:
            self.__equipment_visible = False
            self.__view.hide_inventory()

    def variant_clicked(self, id: int):
        variant = self.__current_variatns.get(id)
        if 'log_author' in variant:
            self.__view.set_log_text_color(self.SELF_COLOR)
            self.__view.add_text_to_log(variant['log_author'])
            self.__view.set_log_text_color(self.BASIC_COLOR)
        self.__view.insert_text_to_log(variant['log_text'])
        self.__current_message_id = variant['next_message_id']
        if self.__current_message_file != variant['next_message_file']:
            self.__current_message_file = variant['next_message_file']
            self.read_new_message_file()
        #self.__view.insert_text_to_log(variant.find('log_text').text)
        #self.__current_message_id = int(variant.find('next_message_id').text)
        self.__print_message()

    def move_to_location(self, location: Location):
<<<<<<< HEAD
        self.__view.add_text_to_log("Вы идете в ")
        self.__view.insert_text_to_log(location.name)
        self.set_current_location(location.id)

    def talk_with_person(self, person: Npc):
        pass
=======
        self.set_current_location(location.id)

    def talk_with_person(self, person):
        pass
>>>>>>> d6a8104500dadcdd058fd3b8745ce852dba376b6
