from components.component import Component
from components.components_enum import ComponentsEnum
from messages.message import Message
from messages.message_code import MessageCode

class RaceComponent(Component):
  def __init__(self, name:str):
    super().__init__(ComponentsEnum.RACE)
    self._name:str = name
  
  def receive(self, message:Message):
    if message._code == MessageCode.SHOW_CHARACTER_INFO:
      message.addAnswer(self._id, str(self))

  def __str__(self):
    return self._name
    
class Orc(RaceComponent):
  def __init__(self):
    super().__init__("Орк")

  def recieve(self, message:Message):
    if message._code == MessageCode.SHOW_CHARACTER_INFO:
      message.addAnswer(self._id, str(self))

  def __str__(self):
    return self._name


class Elf(RaceComponent):
  def __init__(self):
    super().__init__("Эльф")

  def receive(self, message:Message):
    if message._code == MessageCode.SHOW_CHARACTER_INFO:
      message.addAnswer(self._id, str(self))

  def __str__(self):
    return self._name
