from components.component import Component
from components.components_enum import ComponentsEnum
from messages.message import GetParametersMessage, Message
from messages.message_code import MessageCode
from service_objects import ServiceObjects

class AbilityComponent(Component):
  def __init__(self):
    super().__init__(ComponentsEnum.ABILITY)
    self._player = ServiceObjects().game.player

class ThickSkin(AbilityComponent):
  """Способоность "Толстая кожа". Дает 1 ед. брони за каждые 100 хп"""
  def __init__(self):
    super().__init__()
  
  def recieve(self, message: Message):
    if message.code == MessageCode.GET_ARMOR:
      phys_mes = GetParametersMessage(MessageCode.GET_PHYSIQUE)
      self._player.send(phys_mes)
      try:
        physique:int = int(phys_mes.getAnswer(ComponentsEnum.PHYSIQUE))
      except ValueError:
        physique:int = 0
      message.addAnswer(ComponentsEnum.ARMOR, int(physique/100))
