from components.components_enum import ComponentsEnum
from controllers.character_details_controller import CharacterDetailsController
from equipment import Equipment, Weapon, Armor
from creature import Creature, Human
from models.menu_factory import CharacterMenuModelFactory, MainMenuModelFactory
from output import ConsoleOutputComponent
from stats_requirements import WeaponStatsRequirmentsComponent, ArmorStatsRequirmentsComponent
from components.stats_component import FighterStatsComponent
from components.trade_component import TradeComponent
from components.inventory_component import InventoryComponent
from screen import NewGameScreen
from input_component import ConsoleInputComponent
from stats_requirements import WeaponStatsRequirmentsComponent
from message import DescriptionMessage, Message, UpgradeStatsMessage, LevelUpMessage
from message_code import MessageCode
from screens_enum import ScreensEnum
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
    inv_component.addEquipment(Weapon("Палка копалка", 20, 2, WeaponStatsRequirmentsComponent(2,2)))
    inv_component.addEquipment(Weapon("Нож", 50, 5, WeaponStatsRequirmentsComponent(5,5)))
    self._trader.send(Message(MessageCode.ADD_INVENTORY, TradeComponent, inv_component))
    self._trader.name = "Оружейник"
    self._controller = None
  
  def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Game, cls).__new__(cls)
        return cls.instance

  def setNextScreen(self, screen):
    if screen == ScreensEnum.MAIN_MENU:
      model = MainMenuModelFactory().create()
      view = MenuView(model)
      self.controller = MenuController(self, model, view)
      self.ontroller.start()
    if screen == ScreensEnum.CHARACTER_MENU:
      model = CharacterMenuModelFactory().create()
      view = MenuView(model)
      self.controller = MenuController(self, model, view)
      self.controller.start()
    if screen == ScreensEnum.CHARACTER_DETAILS:
      model = self._player.getComponnent(ComponentsEnum.STATS)
      view = MenuView(model)
      self.controller = CharacterDetailsController(self, model)

      self.controller.start()

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
  
  
