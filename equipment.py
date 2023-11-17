from entity import Entity
from abc import abstractmethod

class Equipment(Entity):
  def __init__(self, name, price, stats_requirements):
    self._name = name
    self._price = price
    self._stats_requierments = stats_requirements

  @abstractmethod
  def equip(self, entity, output):
    pass

  @property
  def name(self):
    return self._name


class Weapon(Equipment):
  def __init__(self, name, price, stats_requirements):
    super().__init__(name, price, stats_requirements)

  def equip(self, entity, output):
    if self._stats_requierments.isSatisfyRequirements(entity.stats, output):
      output.out(f"Вы экипировали {self._name}")
      

class Armor(Equipment):
  def __init__(self, name, price, stats_requirements):
    super().__init__(name, price, stats_requirements)

  def equip(self, entity, output):
    if self._stats_requierments.isSatisfyRequirements(entity.stats, output):
      output.out(f"Вы экипировали {self._name}")
