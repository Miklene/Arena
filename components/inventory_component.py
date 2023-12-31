from components.component import Component
from components.components_enum import ComponentsEnum
from screens.equipment import Armor, Weapon


def sortByPrice(equipment):
  return equipment.price

class InventoryComponent(Component):
  def __init__(self):
    super().__init__(ComponentsEnum.INVENTORY)
    self._sections = []

  @property
  def equipment(self):
    return self._equipment
    
  def addEquipment(self, equipment):
    if not self.addEquipmentToSection(equipment):
      self._sections.append(InventorySection(type(equipment).__name__))
      self.addEquipmentToSection(equipment)
  
  def addEquipmentToSection(self, equipment):
    for section in self._sections:
      if section.name == type(equipment).__name__:
        section.addEquipment(equipment)
        return True
    return False

  def showEquipment(self, output, type):
    for section in self._sections:
      if section.name == type(type).__name__():
        section.showEquipment(output)
  
  def isEquipmentExist(self, index, type):
    for section in self._sections:
      if section.name == type(type).__name__():
        return section.isEquipmentExist(index)
  
  def getEquipmentByIndex(self, index, type):
    for section in self._sections:
      if section.name == type(type).__name__():
        return section.getEquipmentByIndex(index)

  def recieve(self, message):
    if not isinstance(self, message.recipient):
      return

class InventorySection:
  def __init__(self, name):
    self._name = name
    self._items = []     

  def addEquipment(self, equipment):
    self._items.append(equipment)
    self._items = sorted(self._items, key=sortByPrice)

  def showEquipment(self, output):
    for equimpent in self._items:
      equimpent.show(output, self._items.index(equimpent) + 1)
      output.out("\n")  

  def isEquipmentExist(self, index):
    if index < 0 or index > len(self._items):
      return False
    return True
  
  def getEquipmentByIndex(self, index):
    if self.isEquipmentExist(index):
      return self._items[index]

  @property
  def name(self):
    return self._name
