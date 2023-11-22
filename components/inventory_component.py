from components.component import Component
from components.components_enum import ComponentsEnum


def sortByPrice(equipment):
  return equipment.price

class InventoryComponent(Component):
  def __init__(self):
    super().__init__(ComponentsEnum.INVENTORY)
    self._equipment = []

  @property
  def equipment(self):
    return self._equipment
    
  def addEquipment(self, equipment):
    self._equipment.append(equipment)
    self._equipment = sorted(self._equipment, key=sortByPrice)
  
  def showEquipment(self, output):
    for equimpent in self._equipment:
      equimpent.show(output, self._equipment.index(equimpent) + 1)
      output.out("\n")
  
  def isEquipmentExist(self, index):
    if index < 0 or index > len(self._inventory):
      return False
    return True
  
  def getEquipmentByIndex(self, index):
    if self.isEquipmentExist(index):
      return self._equipment[index]

  def recieve(self, message):
    if not isinstance(self, message.recipient):
      return
