from abc import ABC, abstractmethod


class StatsComponent(ABC):
  def __init__(self):
    pass
    
  @abstractmethod
  def getDescription(self):
    pass


class FighterStatsComponent(StatsComponent):
  
  def __init__(self, physique, strength, agility):
    super().__init__()
    self._physique = physique
    self._strength = strength
    self._agility = agility

  def getDescription(self):
    description = "\nТелосложение: " + str(self._physique)
    description += "\nСила: " + str(self._strength)
    description += "\nЛовкость: " + str(self._agility)
    return description
    
  @property
  def physique(self):
    return self._physique

  @property
  def strength(self):
    return self._strength

  @property
  def agility(self):
    return self._agility
    
class WeaponStatsComponent(StatsComponent):
  
  def __init__(self, damage):
    super().__init__()
    self._damage = damage

  def getDescription(self):
    description = "\nУрон " + str(self.damage)
    return description
    
  @property
  def damage(self):
    return self._damage

class ArmorStatsComponent(StatsComponent):
  def __init__(self, armor):
    super().__init__()
    self._armor = armor

  def getDescription(self):
    description = "\nБроня: " + str(self.armor)
    return description
    
  @property
  def armor(self):
    return self._armor