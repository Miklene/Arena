from entity import Entity
from stats_component import FighterStatsComponent
from parameters_component import FighterParametersComponent
from equipment_slot_component import ArmorEquipmentSlot, WeaponEquipmentSlot

class Fighter(Entity):
  
  def __init__(self):
    self._components = []
    self._name = ""
    self._race = "No race"
    #self._stats = stats
    #self._parameters = FighterParametersComponent(self._stats)
    #self._equipment_slots = []

  def addComponent(self, component):
    self._components.append(component)

  def send(self, message):
    for component in self._components:
      component.recieve(message)
    
  @property
  def race(self):
    return self._race
    
  @property
  def name(self):
    return self._name
   
  @name.setter
  def name(self, name):
    self._name = name
  
  #def getDescription(self):
  #  description = self._race
  #  description += self._stats.getDescription()
  #  description += self._parameters.getDescription()
  #  for equimpent_slot in self._equipment_slots:
  #    description += equimpent_slot.getDescription()
  # return description


class Orc(Fighter):
  def __init__(self):
    super().__init__()
    self._race = "Орк"
    stats = FighterStatsComponent(10,9,6)
    self.addComponent(stats)
    self.addComponent(FighterParametersComponent(stats))
    self.addComponent(WeaponEquipmentSlot("Правая рука", None))
    self.addComponent(ArmorEquipmentSlot("Тело", None))
 

class Human(Fighter):
  def __init__(self):
    super().__init__()
    self._race = "Человек"
    stats = FighterStatsComponent(9,9,7)
    self.addComponent(stats)
    self.addComponent(FighterParametersComponent(stats))
    self.addComponent(WeaponEquipmentSlot("Правая рука", None))
    self.addComponent(ArmorEquipmentSlot("Тело", None))


class Elf(Fighter):
  def __init__(self):
    super().__init__()
    self._race = "Эльф"
    stats = FighterStatsComponent(8,8,9)
    self.addComponent(stats)
    self.addComponent(FighterParametersComponent(stats))
    self.addComponent(WeaponEquipmentSlot("Правая рука", None))
    self.addComponent(ArmorEquipmentSlot("Тело", None))
    
