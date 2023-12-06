from abc import ABC, abstractmethod
from components.name_component import NameComponent
from controllers.menu_controller import MenuController
from entities.creature import Orc, Elf, Human
from models.menu_factory import MainMenuModelFactory
from output import ConsoleOutputComponent
from messages.message import DescriptionMessage, Message, UpgradeStatsMessage, LevelUpMessage
from messages.message_code import MessageCode
from contextlib import suppress
from components.level_component import LevelComponent
from components.stats_component import StatsComponent
from components.parameters_component import ParametersComponent
from components.equipment_slot_component import EquipmentSlot
from components.trade_component import TradeComponent
from screens.screens_enum import ScreensEnum
from views.menu_view import MenuView


class Screen(ABC):
  def __init__(self, game):
    self._game = game
  

  @abstractmethod
  def start(self, output, inp):
    pass
    

class NewGameScreen(Screen):
  def __init__(self, game):
    super().__init__(game)
  

  def start(self, output, inp):
    self._output = output
    while True:
      race = inp.read("В игре есть три расы: орк, человек, эльф. Введите:\n1 - орк\n2 - человек\n3 - эльф\n")
      if race == "1":
        output.out("")
        self.showDescriptionForStartMenu(Orc())
        accept = inp.read("1 - выбрать\n0 - назад\n")
        if accept == "1":
          player = Orc()
          break
      elif race == "2":
        output.out("")
        self.showDescriptionForStartMenu(Human())
        accept = inp.read("1 - выбрать\n0 - назад\n")
        if accept == "1":
          player = Human()
          break
      elif race == "3":
        output.out("")
        self.showDescriptionForStartMenu(Elf())
        accept = inp.read("1 - выбрать\n0 - назад\n")
        if accept == "1":
          player = Elf()
          break
    name = inp.read("Введите свое имя: ")
    #player.name = name
    self._game.player = player
    self._game.player.name = name
    output.out(f"Добро пожаловать на арену, {player.race} {player.name}")
    self._game.player.send(LevelUpMessage(None))
    self._game.player.send(Message(MessageCode.ADD_MONEY, TradeComponent, 100))
    #MainMenuScreen(self._game).start(output, inp)
    self._game.setNextScreen(ScreensEnum.MAIN_MENU)



  def showDescriptionForStartMenu(self, creature):
    #components_list = [None, LevelComponent, StatsComponent, ParametersComponent]
    #for component in components_list:
    message = DescriptionMessage(self._output, object)
    creature.send(message)
    message.printAnswers()


class MainMenuScreen(Screen):
  def __init__(self, game):
    super().__init__(game)

  def start(self, output, inp):
    while True:
      output.out("\nГлавное меню")
      output.out("У вас: ")
      self._game.player.send(Message(MessageCode.SHOW_MONEY))
      self._game.player.send(Message(MessageCode.SHOW_POINTS))
      choiсe = inp.read("1 - меню персонажа\n2 - меню магазина\n3 - меню боя\n")
      if choiсe == "1":
        CharacterMenuScreen(self._game).start(output, inp)
      if choiсe == "2":
        StoreMenuScreen(self._game).start(output, inp)
      #if choiсe == "3":
      #  self.fightMenu()  

class CharacterMenuScreen(Screen):
  def __init__(self, game):
    super().__init__(game)

  def start(self, output, inp):
    while True:
      output.out("\nМеню персонажа")
      output.out("У вас: ")
      self._game.player.send(Message(MessageCode.SHOW_CHARACTER_INFO, TradeComponent))
      self._game.player.send(Message(MessageCode.SHOW_POINTS))
      choiсe = inp.read("1 - характеристики персонажа\n2 - распределить очки умений\n3 - инвентарь\n0 - назад\n")
      if choiсe == "1":
        output.out("")
        self._game.player.send(DescriptionMessage(output, None))
        self._game.player.send(DescriptionMessage(output, LevelComponent))
        self._game.player.send(DescriptionMessage(output, StatsComponent))
        self._game.player.send(DescriptionMessage(output, ParametersComponent))
        self._game.player.send(DescriptionMessage(output, EquipmentSlot))
      elif choiсe == "2":
        PointsMenuScreen(self._game).start(output, inp)
      #elif choiсe == "3":
      #  self.player.inventoryMenu()
      elif choiсe == "0":
        break

class PointsMenuScreen(Screen):
  def __init__(self, game):
    super().__init__(game)
  
  def start(self, output, inp):
    while True:
      output.out("\nМеню очков умений")
      output.out("У вас: ")
      self._game.player.send(Message(MessageCode.SHOW_POINTS))
      choiсe = inp.read("1 - увеличить телосложение\n2 - увеличить силу\n3 - увеличить ловкость\n4 - подсказка по очкам умений\n0 - назад\n")
      with suppress(ValueError):
        if choiсe == "1":
          points = int(input("Телосложение, введите количество очков:"))
          self._game.player.send(UpgradeStatsMessage({"physique" : points}))
        if choiсe == "2":
          points = int(input("Сила, введите количество очков:"))
          self._game.player.send(UpgradeStatsMessage({"strength" : points}))
        if choiсe == "3":
          points = int(input("Ловкость, введите количество очков:"))
          self._game.player.send(UpgradeStatsMessage({"agility" : points}))
        if choiсe == "4":
          self._game.player.send(Message(MessageCode.SHOW_PARAMETERS_PER_STATS))
        if choiсe == "0":
          break


class StoreMenuScreen(Screen):
  def __init__(self, game):
    super().__init__(game)
  
  def start(self, output, inp):
    while True:
      output.out("\nМеню магазина")
      output.out("У вас: ")
      self._game.player.send(Message(MessageCode.SHOW_CHARACTER_INFO, TradeComponent))
      choiсe = inp.read("1 - оружие\n2 - броня\n0 - назад\n")
      if choiсe == "1":
        self._game.trader.send(Message(MessageCode.BEGIN_TRADE, TradeComponent, self._game.player))
        #self.concreteStoreMenu(self.weapon_store)
        #self.weapon_store.menu(self.player)
      #if choiсe == "2":
        #self.concreteStoreMenu(self.armor_store)
        #self.armor_store.menu(self.player)
      if choiсe == "0":
        break
