from components.level_component import LevelComponent
from components.name_component import NameComponent
from components.race_component import RaceComponent
from entities.entity import Entity
from components.stats_component import FighterStatsComponent
from components.parameters_component import FighterParametersComponent
from components.equipment_slot_component import ArmorEquipmentSlot, WeaponEquipmentSlot
from components.trade_component import TradeComponent
from entities.fightable import Fightable
from messages.message_code import MessageCode
from service_objects import ServiceObjects

class Creature(Entity, Fightable):
  
  def __init__(self, stats):
    super().__init__()
    self._stats = stats
    self.addComponent(self._stats)
    self._level = LevelComponent(self._stats, 20, 2)
    self.addComponent(self._level)
    self._parameters = FighterParametersComponent(self._stats)
    self.addComponent(self._parameters)
    self.addComponent(TradeComponent())
    #self._equipment_slots = []

  def send(self, message):
    #if message.recipient is None:
    #  if message.code == MessageCode.SHOW_CHARACTER_INFO:
    #    output = ServiceObjects().output
    #    output.out(f"{self._race} {self._name}")
    #    return
      #output.out(self._level.getDescription())
      #output.out(self._stats.getDescription())
      #output.out(self._parameters.getDescription())
    super().send(message)   

  def joinBattle(self, opponent):
    self._opponent = opponent
    

  def update(self, delta, pause):
    pass

  def attack(self):
    self._opponent.receive_damage

  def receive_damage(self, damage): 
    pass

  @property
  def stats(self):
    return self.stats


class Orc(Creature):
  def __init__(self):
    super().__init__(FighterStatsComponent(10,9,6))
    self.addComponent(RaceComponent("Орк"))
    self.addComponent(WeaponEquipmentSlot("Правая рука", None))
    self.addComponent(ArmorEquipmentSlot("Тело", None))
 

class Human(Creature):
  def __init__(self):
    super().__init__(FighterStatsComponent(9,9,7))
    self.addComponent(RaceComponent("Человек"))
    self.addComponent(WeaponEquipmentSlot("Правая рука", None))
    self.addComponent(ArmorEquipmentSlot("Тело", None))


class Elf(Creature):
  def __init__(self ):
    super().__init__(FighterStatsComponent(8,8,9))
    self.addComponent(RaceComponent("Эльф"))
    self.addComponent(WeaponEquipmentSlot("Правая рука", None))
    self.addComponent(ArmorEquipmentSlot("Тело", None))
    
