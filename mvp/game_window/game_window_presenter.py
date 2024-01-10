from entities.creature import Creature
from mvp.game_window.game_window_view import GameWindowView


class GameWindowPresenter:
    def __init__(self, view, player: Creature):
        self.__view: GameWindowView = view
        self.__player: Creature = player

    def button_stats_clicked(self):
        pass

    def button_abilities_clicked(self):
        pass

    def button_equipment_clicked(self):
        pass
