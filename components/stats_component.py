from abc import ABC, abstractmethod
from contextlib import suppress
from enum import Enum

from components.component import Component
from components.components_enum import ComponentsEnum
from messages.message import Message, UpdateParameterspMessage
from messages.message_code import MessageCode
from service_objects import ServiceObjects


class StatsObserver(ABC):
  def __init__(self):
    super().__init__()
    pass

  @abstractmethod
  def update(self):
    pass


class StatsObservable:
  def __init__(self):
    self._observers: list[StatsObserver]= []

  def addObserver(self, observer: StatsObserver):
    self._observers.append(observer)
    observer.update()

  def notifyUpdate(self):
    for observer in self._observers:
      observer.update()

  def removeObserver(self, observer):
    with suppress(ValueError):
      self._observers.remove(observer)


class StatsComponent(Component, StatsObservable):
  def __init__(self):
    Component.__init__(self, ComponentsEnum.STATS)
    StatsObservable.__init__(self)

  @abstractmethod
  def getDescription(self):
    pass

  def recieve(self, message:Message):
    if not isinstance(self, message.recipient):
      return
    if message.code == MessageCode.SHOW_CHARACTER_INFO:
      message.addAnswer(self._id, self.getDescription())
      #message.object.out(self.getDescription())

class StatsEnum(Enum):
  PHYSIQUE = 1
  STRENGTH = 2
  AGILITY = 3
  WEAPON_DAMAGE = 4
  ARMOR = 5

class FighterStatsComponent(StatsComponent):
  """Класс компонента характеристик для Creature"""
  def __init__(self, physique: int, strength: int, agility: int):
    """Инициализация компонента характеристик
      - physique - телосложение
      - strength - сила
      - agility - ловкость"""
    super().__init__()
    self._physique = physique
    self._strength = strength
    self._agility = agility

  def getDescription(self):
    description = "Телосложение: " + str(self._physique)
    description += "\nСила: " + str(self._strength)
    description += "\nЛовкость: " + str(self._agility)
    return description

  def increasePhysique(self, value):
    self._physique += value
    self.notifyUpdate()
    #ServiceObjects().game.player.send(UpdateParameterspMessage(None))

  def increaseStrength(self, value):
    self._strength += value
    self.notifyUpdate()
    #ServiceObjects().game.player.send(UpdateParameterspMessage(None))

  def increaseAgility(self, value):
    self._agility += value
    self.notifyUpdate()
    #ServiceObjects().game.player.send(UpdateParameterspMessage(None))

  @property
  def physique(self):
    return self._physique

  @property
  def strength(self):
    return self._strength

  @property
  def agility(self):
    return self._agility


class WeaponStatsComponent(StatsComponent):

  def __init__(self, damage):
    super().__init__()
    self._damage = damage

  def getDescription(self):
    description = "\nУрон " + str(self.damage)
    return description

  @property
  def damage(self):
    return self._damage


class ArmorStatsComponent(StatsComponent):
  def __init__(self, armor):
    super().__init__()
    self._armor = armor

  def getDescription(self):
    description = "\nБроня: " + str(self.armor)
    return description

  @property
  def armor(self):
    return self._armor
