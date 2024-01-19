from components.component import Component
from components.components_enum import ComponentsEnum
from world.quest import Quest


class JournalComponent(Component):

    def __init__(self):
        super().__init__(ComponentsEnum.JOURNAL)
        self.__quests: list[Quest] = []

    def add_quest(self, quest: Quest):
        self.__quests.append(quest)

    def recieve(self, message):
        if not isinstance(self, message.recipient):
            return
