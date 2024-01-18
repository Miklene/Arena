from enum import Enum
from entities.entity import Entity
from abc import abstractmethod

from stats_requirements import WeaponStatsRequirmentsComponent


class EquipmentType(Enum):
  WEAPON = 0,
  ARMOR = 1,


class Equipment(Entity):
  def __init__(self, type: EquipmentType, id,  name, price, stats_requirements):
    self._id = id
    self.__type = type
    self._name = name
    self._price = price
    self._stats_requierments = stats_requirements

  @abstractmethod
  def equip(self, entity, output):
    pass

  @property
  def id(self):
    return self._id

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
  def __init__(self, id,  name, price, damage, stats_requirements: WeaponStatsRequirmentsComponent):
    super().__init__(EquipmentType.WEAPON, id, name, price, stats_requirements)
    self._damage = damage

  def equip(self, entity, output):
    if self._stats_requierments.isSatisfyRequirements(entity.stats, output):
      output.out(f"Вы экипировали {self._name}")

  def show(self, output, index = ""):
    output.out(f"{index}. {self._name}")
    output.out(f"Стоимость {self._price}")
    output.out(f"Урон {self._damage}")
    self._stats_requierments.show(output)

  @property
  def damage(self):
    return self._damage

  @property
  def stats_requierments(self) -> WeaponStatsRequirmentsComponent:
    return self._stats_requierments

  def __str__(self):
    return self.name

class Armor(Equipment):
  def __init__(self, id, name, price, armor, stats_requirements):
    super().__init__(EquipmentType.ARMOR, id,  name, price, stats_requirements)
    self._armor = armor

  def equip(self, entity, output):
    if self._stats_requierments.isSatisfyRequirements(entity.stats, output):
      output.out(f"Вы экипировали {self._name}")

  def show(self, output, index = ""):
    output.out(f"{index}. {self._name}")
    output.out(f"Стоимость {self._price}")
    output.out(f"Броня {self._armor}")
    self._stats_requierments.show(output)
