from mvp.main_menu.main_menu_view import MainMenuView
from components.level_component import *
from components.stats_component import *
from components.name_component import *
from components.parameters_component import *
from components.inventory_component import *
from entities.creature import Creature
from stats_requirements import WeaponStatsRequirmentsComponent


class MainMenuPresenter:

    def __init__(self, view: MainMenuView) -> None:
        self.__view = view

    def button_new_game_clicked(self):
        stats = FighterStatsComponent(5, 5, 5)
        player:Creature = Creature(stats)
        player.addComponent(LevelComponent(stats=stats, initial_points=0))
        #player.addComponent(NameComponent(self.__player_name))
        player.addComponent(FighterParametersComponent(stats))
        player.addComponent(InventoryComponent())
        inventory: InventoryComponent = player.getComponent(ComponentsEnum.INVENTORY)
        inventory.addEquipment(Weapon("Серп", 2, 6, WeaponStatsRequirmentsComponent(4,4)))
        self.__view.start_new_game(player)
