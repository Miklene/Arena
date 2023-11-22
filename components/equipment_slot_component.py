from components.component import Component
from message_code import MessageCode

class EquipmentSlot(Component):
  def __init__(self, name, equipment):
    super().__init__(name)
    self._name = name
    self._equipment = equipment
  
  def recieve(self, message):
    if not isinstance(self, message.recipient):
      return
    if message.code == MessageCode.SHOW_DESCRIPTION:
      message.object.out(self.getDescription())

  def getDescription(self):
    description = f"{self.name}: "
    if self._equipment is None:
      description += "ничего"
    else:
      description += self.equipment.name
    return description

  @property
  def equipment(self):
    return self._equipment

  @equipment.setter
  def equipment(self, equipment):
    self._equipment = equipment

  @property
  def name(self):
    return self._name


class WeaponEquipmentSlot(EquipmentSlot):
  def __init__(self, name, weapon):
    super().__init__(name, weapon)

class ArmorEquipmentSlot(EquipmentSlot):
  def __init__(self, name, armor):
    super().__init__(name, armor)
