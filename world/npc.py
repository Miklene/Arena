from components.inventory_component import InventoryComponent
from components.stats_component import FighterStatsComponent
from entities.creature import Creature
from mvp.game_window.game_window_view import GameWindowView
from world.answer_variant import AnswerVariant
from world.dialog import Dialog
from world.colors import Colors
import json


class Npc(Creature):
    def __init__(self, id: str, name:str, stats:FighterStatsComponent):
        super().__init__(stats)
        self.__id: str = id
        self.__name: str = name
        self.__dialogs: list [Dialog] = []
        self.__current_dialog_id: str = ""
        self.__current_dialog = None

        self.addComponent(InventoryComponent())

        self.__dialogs_file = "strings/dialogs.json"
        with open(self.__dialogs_file, encoding='utf-8') as json_file:
            json_content = json_file.read()
        parsed_json = json.loads(json_content)
        dialogs_json = parsed_json['dialogs']

        self.__parse_dialogs(dialogs_json)

    def __parse_dialogs(self, dialogs_json):
        for d in dialogs_json:
            if d['author_id'] == self.__id:
                dialog = Dialog(d['id'], d['author_id'], d['text'], d['type'])
                variants = []
                if 'variants' in d:
                    for v in d['variants']:
                        variant = AnswerVariant(v['id'], v['text'], v['next_dialog_id'], v['log_text'])
                        variants.append(variant)
                    dialog.variants = variants
                elif 'next_dialog_id' in d:
                    dialog.next_dialog_id = d['next_dialog_id']
                self.__dialogs.append(dialog)

    def talk(self, view: GameWindowView):
        view.clear_variants()
        view.set_log_text_color(Colors.OPPONENT_COLOR.value[0])
        view.add_text_to_log(self.name + ": ")
        view.set_log_text_color(Colors.BASIC_COLOR.value[0])
        view.insert_text_to_log(self.__current_dialog.text)
        variants: list[AnswerVariant] = self.__current_dialog.variants
        for variant in variants:
            view.add_variant(variant.text, variant.id)
        if len(variants) == 0:
            if self.__current_dialog.next_dialog_id != "":
                self.current_dialog_id = self.__current_dialog.next_dialog_id
                self.talk(view)


    def variant_clicked(self, variant_id, view: GameWindowView):
        for v in self.__current_dialog.variants:
            if v.id == variant_id:
                view.set_log_text_color(Colors.SELF_COLOR.value[0])
                view.add_text_to_log("Вы: ")
                view.set_log_text_color(Colors.BASIC_COLOR.value[0])
                view.insert_text_to_log(v.log_text)
                self.current_dialog_id = v.next_dialog_id
        self.talk(view)

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def dialogs(self) -> list[Dialog] :
        return self.__dialogs

    @property
    def current_dialog_id(self) -> str:
        return self.__current_dialog_id

    @current_dialog_id.setter
    def current_dialog_id(self, id: str) -> None:
        self.__current_dialog_id = id
        for dialog in self.__dialogs:
            if dialog.id == self.__current_dialog_id:
                self.__current_dialog = dialog
