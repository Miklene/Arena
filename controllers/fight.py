from components.components_enum import ComponentsEnum
from components.name_component import NameComponent
from controllers.controller import Controller
from entities.creature import Creature
from messages.message import Message
from messages.message_code import MessageCode

class FightController(Controller):
  def __init__(self, game, fighter1:Creature, fighter2:Creature) -> None:
    super().__init__(game,)
    self.fighter1 = fighter1

  def start(self):
    print("Начинается бой")
    delta = 0
    message = Message(MessageCode.SHOW_CHARACTER_INFO, recipient=NameComponent)
    self.fighter1.send(message)
    name = message.getAnswer(ComponentsEnum.NAME)
    print(name)
    while True:
      type = input("Начать бой: \n1 - быстрый бой\n2 - подробный бой\n3 - установить скорость подробного боя\n0 - назад\n")
      if type == "1":
        pause = 0
        break


class Fight:
  def __init__(self,fighter1:Creature, fighter2:Creature) -> None:
    self.fighter1 = fighter1
    self.fighter2 = fighter2
