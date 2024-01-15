from components.stats_component import FighterStatsComponent
from entities.creature import Creature


class Npc(Creature):
    def __init__(self, stats:FighterStatsComponent):
        super().__init__(stats)
