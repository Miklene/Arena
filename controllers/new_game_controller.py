from components.ability_component import ThickSkin
from components.components_enum import ComponentsEnum
from controllers.controller import Controller
from service_objects import ServiceObjects
from entities.creature import Orc, Elf, Human
from messages.message_code import MessageCode
from messages.message import DescriptionMessage, GetParametersMessage, Message, UpgradeStatsMessage, LevelUpMessage
from components.trade_component import TradeComponent
from screens.screens_enum import ScreensEnum


class NewGameController(Controller):
  def __init__(self, game, model):
    super().__init__(game, model)
  
  def start(self):
    inp = ServiceObjects().input
    self._output = ServiceObjects().output
    while True:
      race = inp.read("В игре есть три расы: орк, человек, эльф. Введите:\n1 - орк\n2 - человек\n3 - эльф\n")
      if race == "1":
        self._output.out("")
        self.showDescriptionForStartMenu(Orc())
        accept = inp.read("1 - выбрать\n0 - назад\n")
        if accept == "1":
          player = Orc()
          break
      elif race == "2":
        self._output.out("")
        self.showDescriptionForStartMenu(Human())
        accept = inp.read("1 - выбрать\n0 - назад\n")
        if accept == "1":
          player = Human()
          break
      elif race == "3":
        self._output.out("")
        self.showDescriptionForStartMenu(Elf())
        accept = inp.read("1 - выбрать\n0 - назад\n")
        if accept == "1":
          player = Elf()
          break
    name = inp.read("Введите свое имя: ")
    #player.name = name
    self._game.player = player
    self._game.player.name = name
    message = DescriptionMessage(self._output, object)
    race = player.send(message)
    race = message.getAnswer(ComponentsEnum.RACE)
    self._output.out(f"Добро пожаловать на арену, {race} {player.name}")
    self._game.player.send(LevelUpMessage(None))
    self._game.player.send(Message(MessageCode.ADD_MONEY, TradeComponent, 100))
    #player.addComponent(ThickSkin())
    #message = GetParametersMessage(MessageCode.GET_ARMOR)
    #player.send(message)
    #armor = message.getAnswer(ComponentsEnum.ARMOR)
    #print(f"Броня: {armor}")
    self._game.setNextScreen(ScreensEnum.MAIN_MENU)

  def showDescriptionForStartMenu(self, creature):
    message = DescriptionMessage(self._output, object)
    creature.send(message)
    message.printAnswers()
