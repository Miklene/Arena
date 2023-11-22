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
  
  @property
  def price(self):
    return self._price
  
  @property
  def stats_requierments(self):
    return self._stats_requierments

  @abstractmethod
  def show(self, output, index = ""):
    pass


class Weapon(Equipment):
  def __init__(self, name, price, damage, stats_requirements):
    super().__init__(name, price, stats_requirements)
    self._damage = damage

  def equip(self, entity, output):
    if self._stats_requierments.isSatisfyRequirements(entity.stats, output):
      output.out(f"Вы экипировали {self._name}")
      
  def show(self, output, index = ""):
    output.out(f"{index}. {self._name}")    
    output.out(f"Стоимость {self._price}")    
    output.out(f"Урон {self._damage}")   
    self._stats_requierments.show(output)

class Armor(Equipment):
  def __init__(self, name, price, armor, stats_requirements):
    super().__init__(name, price, stats_requirements)
    self._armor = armor

  def equip(self, entity, output):
    if self._stats_requierments.isSatisfyRequirements(entity.stats, output):
      output.out(f"Вы экипировали {self._name}")

  def show(self, output, index = ""):
    output.out(f"{index}. {self._name}")    
    output.out(f"Стоимость {self._price}")    
    output.out(f"Броня {self._armor}")   
    self._stats_requierments.show(output)
