from components.component import Component

from abc import abstractmethod

from message_code import MessageCode
from service_objects import ServiceObjects

class ParametersComponent(Component):

  HP_PER_PHYSIQUE = 30
  DAMAGE_PER_STRENGTH = 2
  SPEED_PER_AGILITY = 0.2

  def __init__(self, stats):
    pass
  
  def recieve(self, message):
    if message.code == MessageCode.SHOW_DESCRIPTION:
      message.object.out(self.getDescription())
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

  def showParametersPerStats(self):
    message = f"Одно очко телосложения равно {self.HP_PER_PHYSIQUE} очкам здоровья"
    message += f"\nОдно очко силы равно {self.DAMAGE_PER_STRENGTH} единицам урона"
    message += f"\nОдно очко ловкости равно {self.SPEED_PER_AGILITY} скорости атаки"
    ServiceObjects().output.out(message)

class FighterParametersComponent(ParametersComponent):
  def __init__(self, stats):
    super().__init__(stats)
    self._stats = stats
    self.update()

  def getDescription(self):
    description = f"Здоровье: {self._hp}"
    description += f"\nУрон: {self._damage}" 
    description += "\nСкорость атаки: {:.2} ударов в секунду".format(
        self._speed)
    return description
  
  def update(self):
    self._hp = self._stats.physique * self.HP_PER_PHYSIQUE
    self._damage = self._stats.strength * self.DAMAGE_PER_STRENGTH
    self._speed = self._stats.agility * self.SPEED_PER_AGILITY
    self._attack_speed = 1 / self._speed
