from models.menu_model import MenuModel, MenuItem
from abc import ABC, abstractmethod
from screens.screens_enum import ScreensEnum
class MenuModelFactry(ABC):
  @abstractmethod
  def create(self):
    pass

class MainMenuModelFactory(MenuModelFactry):
  def create(self):
    model = MenuModel("\nГлавное меню")
    model.addMenuItem(MenuItem("1", "меню персонажа", ScreensEnum.CHARACTER_MENU))
    model.addMenuItem(MenuItem("2", "меню магазина", ScreensEnum.STORE_MENU))
    model.addMenuItem(MenuItem("3", "меню боя", ScreensEnum.FIGHT_MENU))
    return model

class CharacterMenuModelFactory(MenuModelFactry):
  def create(self):
    model = MenuModel("\nПерсонаж")
    model.addMenuItem(MenuItem("1", "характеристики", ScreensEnum.CHARACTER_DETAILS))
    model.addMenuItem(MenuItem("2", "распределить очки умений", ScreensEnum.CHARACTER_POINTS))
    model.addMenuItem(MenuItem("3", "инвентарь", ScreensEnum.CHARACTER_INVENTORY))
    model.addMenuItem(MenuItem("0", "назад", ScreensEnum.PREVIOUS))
    return model

class StoreMenuModelFactory(MenuModelFactry):
  def create(self):
    model = MenuModel("\nМагазин")
    model.addMenuItem(MenuItem("1", "оружие", ScreensEnum.STORE_WEAPON))
    model.addMenuItem(MenuItem("2", "броня", ScreensEnum.STORE_ARMOR))
    model.addMenuItem(MenuItem("0", "назад", ScreensEnum.PREVIOUS))
    return model
