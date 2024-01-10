from components.level_component import *
from components.stats_component import *
from components.name_component import *
from components.parameters_component import *
from components.inventory_component import *
from entities.creature import Creature
from mvp.new_game_widget.new_game_widget_view import NewGameWidgetView


class NewGameWidgetPresenter:
    def __init__(self, view: NewGameWidgetView) -> None:
        self.__view = view
        self.__player_name: str = ""

    def button_create_clicked(self):
        if self.__player_name != "":
            stats = FighterStatsComponent(5, 5, 5)
            player:Creature = Creature(stats)
            player.addComponent(LevelComponent(stats=stats))
            player.addComponent(NameComponent(self.__player_name))
            player.addComponent(FighterParametersComponent(stats))
            player.addComponent(InventoryComponent())
            self.__view.start_new_game(player)

    def line_edit_text_changed(self, text: str) -> None:
        self.__player_name = text
