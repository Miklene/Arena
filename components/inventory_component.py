from components.component import Component


def sortByPrice(equipment):
  return equipment.price

class InventoryComponent(Component):
  def __init__(self):
    super().__init__()
    self._equipment = []

  def addEquipment(self, equipment):
    self._equipment.append(equipment)
    self._equipment = sorted(self._equipment, key=sortByPrice)
