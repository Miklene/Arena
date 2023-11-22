from components.components_enum import ComponentsEnum
from message import MessageCode
from components.component import Component
from service_objects import ServiceObjects

class LevelComponent(Component):
  def __init__(self, stats, max_level, points_per_level):
    super().__init__(ComponentsEnum.LEVEL)
    self._stats = stats
    self._max_level = max_level
    self._points = 0
    self._point_per_level = points_per_level
    self._current_level = 1
  
  def recieve(self, message):
    if not isinstance(self, message.recipient):
      return
    if message.code == MessageCode.SHOW_DESCRIPTION:
      message.object.out(self.getDescription())
    if message.code == MessageCode.UPGRADE_STATS:
      keys = message.object.keys()
      for key in keys:
        value = message.object.get(key)
        if value > self.points:
            ServiceObjects().output.out("Недостаточно очков")
        else:
          if key == "physique":
            self._stats.increasePhysique(value)
            self._points -= value
            ServiceObjects().output.out(f"Телосложение увеличено на {value}. Текущее значение: {self._stats.physique}")
          if key == "strength":
            self._stats.increaseStrength(value)
            self._points -= value
            ServiceObjects().output.out(f"Сила увеличена на {value}. Текущее значение: {self._stats.strength}")
          if key == "agility":
            self._stats.increaseAgility(value)
            self._points -= value
            ServiceObjects().output.out(f"Ловкость увеличена на {value}. Текущее значение: {self._stats.agility}")
    if message.code == MessageCode.LEVEL_UP:
      self.levelUp()
    if message.code == MessageCode.SHOW_POINTS:
      ServiceObjects().output.out(f"{self._points} нераспределенных очков умений")

  def levelUp(self):
    self._current_level += 1
    self._points += self._point_per_level

  def getDescription(self):
    return f"Уровень: {self._current_level}"

  @property
  def maxLevel(self):
    return self._max_level
  
  @property 
  def points(self):
    return self._points
  
  
  