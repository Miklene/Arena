from components.stats_component import FighterStatsComponent
from entities.creature import Creature


class Npc(Creature):
    def __init__(self, id: str, name:str, stats:FighterStatsComponent):
        super().__init__(stats)
        self.__id = id
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id
