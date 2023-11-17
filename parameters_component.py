from component import Component

from abc import abstractmethod

from message_code import MessageCode

class ParametersComponent(Component):

  HP_PER_PHYSIQUE = 30
  DAMAGE_PER_STRENGTH = 2
  SPEED_PER_AGILITY = 0.2

  def __init__(self, stats):
    pass
  
  @abstractmethod
  def getDescription(self):
    pass
    
  def recieve(self, message):
    if message.code == MessageCode.SHOW_DESCRIPTION:
      message.object.out(self.getDescription())


class FighterParametersComponent(ParametersComponent):
  def __init__(self, stats):
    super().__init__(stats)
    self._hp = stats.physique * self.HP_PER_PHYSIQUE
    self._damage = stats.strength * self.DAMAGE_PER_STRENGTH
    self._speed = stats.agility * self.SPEED_PER_AGILITY
    self._attack_speed = 1 / self._speed

  def getDescription(self):
    description = "Здоровье: " + str(self._hp)
    description += "\nУрон: " + str(self._damage)
    description += "\nСкорость атаки: {:.2} ударов в секунду".format(
        self._speed)
    return description
