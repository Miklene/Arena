from abc import ABC, abstractmethod
from components.name_component import NameComponent
from fighter import Orc, Elf, Human
from output import ConsoleOutputComponent
from message import DescriptionMessage, Message, UpgradeStatsMessage, LevelUpMessage
from message_code import MessageCode
from contextlib import suppress

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
    while True:
      race = inp.read("В игре есть три расы: орк, человек, эльф. Введите:\n1 - орк\n2 - человек\n3 - эльф\n")
      if race == "1":
        output.out("")
        Orc().send(DescriptionMessage(output))
        accept = inp.read("1 - выбрать\n0 - назад\n")
        if accept == "1":
          player = Orc()
          break
      elif race == "2":
        output.out("")
        Human().send(DescriptionMessage(output))
        accept = inp.read("1 - выбрать\n0 - назад\n")
        if accept == "1":
          player = Human()
          break
      elif race == "3":
        output.out("")
        Elf().send(DescriptionMessage(output))
        accept = inp.read("1 - выбрать\n0 - назад\n")
        if accept == "1":
          player = Elf()
          break
    name = inp.read("Введите свое имя: ")
    #player.name = name
    self._game.player = player
    self._game.player.addComponent(NameComponent("name"))
    output.out(f"Добро пожаловать на арену, {player.race} {player.name}")
    self._game.player.send(LevelUpMessage(None))
    MainMenuScreen(self._game).start(output, inp)


class MainMenuScreen(Screen):
  def __init__(self, game):
    super().__init__(game)

  def start(self, output, inp):
    while True:
      output.out("\nГлавное меню")
      self._game.player.send(Message(MessageCode.SHOW_POINTS))
      choiсe = inp.read("1 - меню персонажа\n2 - меню магазина\n3 - меню боя\n")
      if choiсe == "1":
        CharacterMenuScreen(self._game).start(output, inp)
      #if choiсe == "2":
      #  self.storeMenu()
      #if choiсe == "3":
      #  self.fightMenu()  

class CharacterMenuScreen(Screen):
  def __init__(self, game):
    super().__init__(game)

  def start(self, output, inp):
    while True:
      output.out("\nМеню персонажа")
      self._game.player.send(Message(MessageCode.SHOW_POINTS))
      choiсe = inp.read("1 - характеристики персонажа\n2 - распределить очки умений\n3 - инвентарь\n0 - назад\n")
      if choiсe == "1":
        output.out("")
        self._game.player.send(DescriptionMessage(output))
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
