from components.component import Component
from components.components_enum import ComponentsEnum
from screens.equipment import Armor, Equipment, Weapon


def sortByPrice(equipment):
  return equipment.price

class InventoryComponent(Component):
  """Класс компонента инвентаря

  Атрибуты:
  --------
  sections : list[InventorySection]
    - список секций инвентаря
  """
  def __init__(self):
    super().__init__(ComponentsEnum.INVENTORY)
    self._sections: list[InventorySection] = []

  @property
  def equipment(self):
    return self._sections

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

  def isEquipmentExist(self, id, type):
    for section in self._sections:
      if section.name == type(type).__name__():
        return section.isEquipmentExist(id)

  def getEquipmentById(self, id, type):
    for section in self._sections:
      if section.name == type(type).__name__():
        return section.getEquipmentById(id)

  def popEquipmentById(self, id, type):
    for section in self._sections:
      if section.name == type(type).__name__():
        return section.popEquipmentById(id)

  def recieve(self, message):
    if not isinstance(self, message.recipient):
      return

class InventorySection:
  """Класс секции инвентаря

  Атрибуты:
  --------
  name : str
    имя секции
  items: list[Equipment]
    список предметов в секции
  """
  def __init__(self, name: str):
    """Инициализация секции инвентарая"""
    self._name = name
    self.__items: list[Equipment] = []

  def addEquipment(self, equipment: Equipment):
    self.__items.append(equipment)
    self.__items = sorted(self.__items, key=sortByPrice)

  def showEquipment(self, output):
    for equimpent in self.__items:
      equimpent.show(output, self.__items.index(equimpent) + 1)
      output.out("\n")

  def isEquipmentExist(self, id):
    for item in self.__items:
      if item.id == id:
        return True
    return False

  def getEquipmentById(self, id):
    for item in self.__items:
      if item.id == id:
        return item

  def popEquipmentById(self, id):
    for item in self.__items:
      if item.id == id:
        self.__items.remove(item)
        return item

  def len(self):
    return len(self.__items)

  @property
  def name(self):
    return self._name
