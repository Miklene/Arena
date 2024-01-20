from components.components_enum import ComponentsEnum
from components.inventory_component import InventoryComponent
from components.journal_component import JournalComponent
from components.stats_component import FighterStatsComponent
from entities.creature import Creature
from mvp.game_window.game_window_view import GameWindowView
from world.answer_variant import AnswerVariant
from world.dialog import Dialog, DialogAction, DialogActionType
from world.colors import Colors
import json

from world.quest import Quest


class Npc(Creature):
    def __init__(self, id: str, name:str, stats:FighterStatsComponent):
        super().__init__(stats)
        self.__id: str = id
        self.__name: str = name
        self.__dialogs: list [Dialog] = []
        self.__current_dialog_id: str = ""
        self.__current_dialog: Dialog = None

        self.addComponent(InventoryComponent())

        self.__dialogs_file = "strings/dialogs.json"
        self.__quests_file = "strings/quests.json"
        with open(self.__dialogs_file, encoding='utf-8') as json_file:
            json_content = json_file.read()
        parsed_json = json.loads(json_content)
        dialogs_json = parsed_json['dialogs']

        with open(self.__quests_file, encoding='utf-8') as json_file:
            json_content = json_file.read()
        parsed_json = json.loads(json_content)
        quests_json = parsed_json['quests']

        self.__parse_dialogs(dialogs_json, quests_json)
        self.__player = None

    def __parse_dialogs(self, dialogs_json, quests_json):
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
                self.__parse_actions_in_dialog(d, dialog)
                self.__parse_quest_in_dialog(d, dialog, quests_json)
                self.__dialogs.append(dialog)

    def __parse_actions_in_dialog(self, d, dialog: Dialog):
        if "actions" in d:
            for a in d['actions']:
                action = DialogAction(DialogActionType[a['type']], a['text'], a['id'])
                dialog.action = action

    def __parse_quest_in_dialog(self, d, dialog: Dialog, quests_json):
        if 'quest_id' in d:
            for q in quests_json:
                if q['id'] == d['quest_id']:
                    quest = Quest(q['id'], q['name'], q['description'], q['reward_exp'])
                    dialog.quest = quest
                    break

    def talk(self, view: GameWindowView, player: Creature):
        self.__player = player
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
                self.talk(view, self.__player)
        self.__handle_action(view)
        self.__handle_quest(view)

    def __handle_action(self, view: GameWindowView):
        action = self.__current_dialog.action
        if action is not None:
            view.add_text_to_log(action.text + ': ')
            if action.type == DialogActionType.REWARD:
                inventory: InventoryComponent = self.getComponent(ComponentsEnum.INVENTORY)
                if inventory.isEquipmentExist(action.reward_id):
                    item = inventory.popEquipmentById(action.reward_id)
                    view.insert_text_to_log(item.name)
                    player_inventory: InventoryComponent = self.__player.getComponent(ComponentsEnum.INVENTORY)
                    player_inventory.addEquipment(item)

    def __handle_quest(self, view: GameWindowView):
        quest = self.__current_dialog.quest
        if quest is not None:
            view.add_text_to_log('Новый квест: ')
            view.insert_text_to_log(quest.name)
            journal: JournalComponent = self.__player.getComponent(ComponentsEnum.JOURNAL)
            journal.add_quest(quest)

    def variant_clicked(self, variant_id, view: GameWindowView):
        for v in self.__current_dialog.variants:
            if v.id == variant_id:
                view.set_log_text_color(Colors.SELF_COLOR.value[0])
                view.add_text_to_log("Вы: ")
                view.set_log_text_color(Colors.BASIC_COLOR.value[0])
                view.insert_text_to_log(v.log_text)
                self.current_dialog_id = v.next_dialog_id
        self.talk(view, self.__player)

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
