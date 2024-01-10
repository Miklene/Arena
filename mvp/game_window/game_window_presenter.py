from entities.creature import Creature
from mvp.game_window.game_window_view import GameWindowView
import xml.etree.ElementTree as ET

class GameWindowPresenter:
    def __init__(self, view, player: Creature):
        self.__view: GameWindowView = view
        self.__player: Creature = player
        self.__current_message_id = 0
        self.__current_variatns: dict[int, ET.Element] = {}
        self.__root = ET.parse('strings/new_game.xml').getroot()
        self.__print_message()


    def __print_message(self):
        self.__view.clear_variants()
        self.__current_variatns.clear()
        for message in self.__root.findall('message'):
            id = int(message.get('id'))
            if id == self.__current_message_id:
                text = message.find('text')
                self.__view.add_text_to_log(text.text)
                self.__add_variants(message)

    def __add_variants(self, message: ET.Element):
        for variant in message.findall('variant'):
            self.__view.add_variant(variant.find('text').text, int(variant.get('id')))
            self.__current_variatns[int(variant.get('id'))] = variant

    def button_stats_clicked(self):
        pass

    def button_abilities_clicked(self):
        pass

    def button_equipment_clicked(self):
        pass

    def variant_clicked(self, id: int):
        variant = self.__current_variatns.get(id)
        self.__view.insert_text_to_log(variant.find('log_text').text)
        self.__current_message_id = int(variant.find('next_message_id').text)
        self.__print_message()
