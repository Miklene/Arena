from models.menu_model import MenuModel, MenuItem
from abc import ABC, abstractmethod
from screens_enum import ScreensEnum
class MenuModelFactry(ABC):
  @abstractmethod
  def create(self):
    pass

class MainMenuModelFactory(MenuModelFactry):
  def create(self):
    model = MenuModel("\nГлавное меню")
    model.addMenuItem(MenuItem("1", "меню персонажа", ScreensEnum.CHARACTER_MENU))
    model.addMenuItem(MenuItem("2", "меню магазина", None))
    model.addMenuItem(MenuItem("3", "меню боя", None))
    return model

class CharacterMenuModelFactory(MenuModelFactry):
  def create(self):
    model = MenuModel("\nГлавное меню")
    model.addMenuItem(MenuItem("1", "характеристики", ScreensEnum.CHARACTER_DETAILS))
    model.addMenuItem(MenuItem("2", "распределить очки умений", ScreensEnum.CHARACTER_POINTS))
    model.addMenuItem(MenuItem("3", "инвентарь", ScreensEnum.CHARACTER_INVENTORY))
    model.addMenuItem(MenuItem("0", "назад", ScreensEnum.MAIN_MENU))
    return model
  