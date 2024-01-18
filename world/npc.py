from components.stats_component import FighterStatsComponent
from entities.creature import Creature
from world.dialog import Dialog


class Npc(Creature):
    def __init__(self, id: str, name:str, stats:FighterStatsComponent):
        super().__init__(stats)
        self.__id: str = id
        self.__name: str = name
        self.__dialogs: list [Dialog] = []

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def dialogs(self) -> list[Dialog] :
        return self.__dialogs

    @dialogs.setter
    def dialogs(self, dialogs: list[Dialog]) -> None :
        self.__dialogs = dialogs
