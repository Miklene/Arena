from components.stats_component import FighterStatsComponent
from entities.creature import Creature
from world.answer_variant import AnswerVariant
from world.dialog import Dialog
import json


class Npc(Creature):
    def __init__(self, id: str, name:str, stats:FighterStatsComponent):
        super().__init__(stats)
        self.__id: str = id
        self.__name: str = name
        self.__dialogs: list [Dialog] = []
        self.__dialogs_file = "strings/dialogs.json"
        with open(self.__dialogs_file, encoding='utf-8') as json_file:
            json_content = json_file.read()
        parsed_json = json.loads(json_content)
        dialogs_json = parsed_json['dialogs']
        self.parse_dialogs(dialogs_json)


    def parse_dialogs(self, dialogs_json):
        for d in dialogs_json:
            if d['author_id'] == self.__id:
                dialog = Dialog(d['id'], d['author_id'], d['text'], d['type'])
                variants = []
                for v in d['variants']:
                    variant = AnswerVariant(v['id'], v['text'], v['next_dialog_id'], v['log_text'])
                    variants.append(variant)
                dialog.variants = variants
                self.__dialogs.append(dialog)

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def dialogs(self) -> list[Dialog] :
        return self.__dialogs

    #@dialogs.setter
    #def dialogs(self, dialogs: list[Dialog]) -> None :
    #    self.__dialogs = dialogs
