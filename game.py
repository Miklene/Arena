from queue import LifoQueue
from components.components_enum import ComponentsEnum
from controllers.character_details_controller import CharacterDetailsController
from controllers.character_points_controller import CharacterPointsController
from controllers.store_controller import StoreController
from screens.equipment import Equipment, Weapon, Armor
from entities.creature import Creature, Human
from models.menu_factory import CharacterMenuModelFactory, MainMenuModelFactory, StoreMenuModelFactory
from output import ConsoleOutputComponent
from stats_requirements import WeaponStatsRequirmentsComponent, ArmorStatsRequirmentsComponent
from components.stats_component import FighterStatsComponent
from components.trade_component import TradeComponent
from components.inventory_component import InventoryComponent
from screens.screen import NewGameScreen
from input_component import ConsoleInputComponent
from stats_requirements import WeaponStatsRequirmentsComponent
from messages.message import DescriptionMessage, Message, UpgradeStatsMessage, LevelUpMessage
from messages.message_code import MessageCode
from screens.screens_enum import ScreensEnum
from views.menu_view import MenuView
from controllers.menu_controller import MenuController


class Game:
  def __init__(self):
    self._output = ConsoleOutputComponent()
    self._input = ConsoleInputComponent()
    self._screen = NewGameScreen(self)
    self._player = None
    self._trader = Human()
    #trade_component = TradeComponent()
    inv_component = InventoryComponent()
    inv_component.addEquipment(Weapon("Палка", 20, 2, WeaponStatsRequirmentsComponent(6, 4)))
    inv_component.addEquipment(Weapon("Нож", 40, 4, WeaponStatsRequirmentsComponent(4, 8)))
    inv_component.addEquipment(Armor("Одежда бомжа", 20, 2, ArmorStatsRequirmentsComponent(8)))
    inv_component.addEquipment(Armor("Укрепленная одежда бомжа", 40, 4, ArmorStatsRequirmentsComponent(10)))
    self._trader.send(Message(MessageCode.ADD_INVENTORY, TradeComponent, inv_component))
    self._trader.name = "Оружейник"
    self._controller = None
    self._controllers_stack = LifoQueue()
  
  def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Game, cls).__new__(cls)
        return cls.instance

  def setNextScreen(self, screen):
    if screen == ScreensEnum.MAIN_MENU:
      model = MainMenuModelFactory().create()
      self._controllers_stack.put(self._controller)
      self._controller = MenuController(self, model)
      self._controller.start()
    if screen == ScreensEnum.CHARACTER_MENU:
      model = CharacterMenuModelFactory().create()
      self._controllers_stack.put(self._controller)
      self._controller = MenuController(self, model)
      self._controller.start()
    if screen == ScreensEnum.CHARACTER_DETAILS:
      model = self._player
      self._controllers_stack.put(self._controller)
      self._controller = CharacterDetailsController(self, model)
      self._controller.start()
    if screen == ScreensEnum.CHARACTER_POINTS:
      self._controllers_stack.put(self._controller)
      model = self._player
      self._controller = CharacterPointsController(self, model)
      self._controller.start()
    if screen == ScreensEnum.STORE_MENU:
      model = StoreMenuModelFactory().create()
      self._controllers_stack.put(self._controller)
      self._controller = MenuController(self, model)
      self._controller.start()
    if screen == ScreensEnum.STORE_WEAPON:
      self._controllers_stack.put(self._controller)
      self._controller = StoreController(self._trader, self._player)
      self._controller.start()
    if screen == ScreensEnum.PREVIOUS:
      if not self._controllers_stack.empty():
        self._controller = self._controllers_stack.get()
        self._controller.start()


  @property
  def controller(self):
    return self._controller
  
  @controller.setter
  def controller(self, controller):
    self._controller = controller

  @property
  def player(self):
    return self._player

  @property
  def output(self):
    return self._output

  @property
  def trader(self):
    return self._trader

  @player.setter
  def player(self, player):
    self._player = player

  def start(self):
    self._screen.start(self._output, self._input)
  
  
