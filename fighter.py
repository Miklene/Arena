from components.level_component import LevelComponent
from components.name_component import NameComponent
from entity import Entity
from components.stats_component import FighterStatsComponent
from components.parameters_component import FighterParametersComponent
from components.equipment_slot_component import ArmorEquipmentSlot, WeaponEquipmentSlot

class Fighter(Entity):
  
  def __init__(self):
    super().__init__()
    self._race = "No race"
    #self._stats = stats
    #self._parameters = FighterParametersComponent(self._stats)
    #self._equipment_slots = []

  @property
  def race(self):
    return self._race
     

class Orc(Fighter):
  def __init__(self):
    super().__init__()
    self._race = "Орк"
    stats = FighterStatsComponent(10,9,6)
    self.addComponent(LevelComponent(stats, 20, 2))
    self.addComponent(stats)
    self.addComponent(FighterParametersComponent(stats))
    self.addComponent(WeaponEquipmentSlot("Правая рука", None))
    self.addComponent(ArmorEquipmentSlot("Тело", None))
 

class Human(Fighter):
  def __init__(self):
    super().__init__()
    self._race = "Человек"
    stats = FighterStatsComponent(9,9,7)
    self.addComponent(LevelComponent(stats, 20, 2))
    self.addComponent(stats)
    self.addComponent(FighterParametersComponent(stats))
    self.addComponent(WeaponEquipmentSlot("Правая рука", None))
    self.addComponent(ArmorEquipmentSlot("Тело", None))


class Elf(Fighter):
  def __init__(self):
    super().__init__()
    self._race = "Эльф"
    stats = FighterStatsComponent(8,8,9)
    self.addComponent(LevelComponent(stats, 20, 2))
    self.addComponent(stats)
    self.addComponent(FighterParametersComponent(stats))
    self.addComponent(WeaponEquipmentSlot("Правая рука", None))
    self.addComponent(ArmorEquipmentSlot("Тело", None))
    
