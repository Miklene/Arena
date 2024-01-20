from components.component import Component

from abc import abstractmethod
from components.components_enum import ComponentsEnum
from components.stats_component import StatsComponent

from messages.message_code import MessageCode
from messages.message import Message
from service_objects import ServiceObjects

class ParametersComponent(Component):
  """Абстрактный класс компонента параметров

  Наследники:
    - FighterParametersComponent
  """

  HP_PER_PHYSIQUE = 30
  DAMAGE_PER_STRENGTH = 2
  SPEED_PER_AGILITY = 0.2

  def __init__(self, stats: StatsComponent):
    super().__init__(ComponentsEnum.PARAMETERS)

  def receive(self, message:Message):
    if not isinstance(self, message.recipient):
      return
    if message.code == MessageCode.SHOW_CHARACTER_INFO:
      message.addAnswer(self._id, self.getDescription())
    if message.code == MessageCode.UPDATE_PARAMETERS:
      self.update()
    if message.code == MessageCode.SHOW_PARAMETERS_PER_STATS:
      self.showParametersPerStats()

  @abstractmethod
  def getDescription(self):
    pass

  @abstractmethod
  def update(self):
    pass

  def get_hint_for_physique(self):
    return f"Одно очко телосложения равно {self.HP_PER_PHYSIQUE} очкам здоровья"

  def get_hint_for_strength(self):
    return f"Одно очко силы равно {self.DAMAGE_PER_STRENGTH} единицам урона"

  def get_hint_for_agility(self):
    return f"Одно очко ловкости равно {self.SPEED_PER_AGILITY} скорости атаки"

  def showParametersPerStats(self):
    message = f"Одно очко телосложения равно {self.HP_PER_PHYSIQUE} очкам здоровья"
    message += f"\nОдно очко силы равно {self.DAMAGE_PER_STRENGTH} единицам урона"
    message += f"\nОдно очко ловкости равно {self.SPEED_PER_AGILITY} скорости атаки"
    return message
    #ServiceObjects().output.out(message)

class FighterParametersComponent(ParametersComponent):

  def __init__(self, stats):
    super().__init__(stats)
    self._stats = stats
    self.update()

  def receive(self, message: Message):
    super().recieve(message)
    if message.code == MessageCode.GET_HP:
      message.addAnswer(ComponentsEnum.HP, self._hp)
    if message.code == MessageCode.GET_CURRENT_HP:
      message.addAnswer(ComponentsEnum.CURRENT_HP, self._current_hp)


  def getDescription(self):
    description = f"Здоровье: {self._hp}"
    description += f"\nУрон: {self._damage}"
    description += "\nСкорость атаки: {:.2} ударов в секунду".format(
        self._speed)
    return description

  def update(self):
    self._hp = int(self._stats.physique * self.HP_PER_PHYSIQUE)
    self._current_hp = self._hp
    self._damage = self._stats.strength * self.DAMAGE_PER_STRENGTH
    self._speed = self._stats.agility * self.SPEED_PER_AGILITY
    self._attack_speed = 1 / self._speed
