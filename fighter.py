from entity import Entity
from stats import FighterStatsComponent

class Fighter(Entity):
  
  def __init__(self):
    self._name = ""
    self._race = "No race"
    self._stats = FighterStatsComponent(5,5,5)

  @property
  def stats(self):
    return self._stats
    
  @property
  def race(self):
    return self._race
    
  @property
  def name(self):
    return self._name
   
  @name.setter
  def name(self, name):
    self._name = name
    
  def getDescription(self):
    description = self._race
    description += self._stats.getDescription()
    return description
    
#class Inventory:
  
class Orc(Fighter):
  def __init__(self):
    super().__init__()
    self._race = "Орк"
    self._stats = FighterStatsComponent(10,9,6)
 
class Human(Fighter):
  def __init__(self):
    super().__init__()
    self._race = "Человек"
    self._stats = FighterStatsComponent(9,9,7)
    
class Elf(Fighter):
  def __init__(self):
    super().__init__()
    self._race = "Эльф"
    self._stats = FighterStatsComponent(8,8,9)