from components.components_enum import ComponentsEnum
from components.stats_component import StatsComponent, StatsEnum
from messages.message_code import MessageCode
from messages.message import Message
from components.component import Component
from service_objects import ServiceObjects

class LevelComponent(Component):
  """Компонент уровень"""
  def __init__(self, stats: StatsComponent,  initial_level: int = 1, max_level: int = 40, initial_points: int = 5,  points_per_level: int = 2):
    """Инициализация компонента уровень
      - stats - компонент характеристик
      - initial_level - начальный уровень персонажа
      - max_level - максимальный уровень персонажа
      - initial_points - начальное количество очков
      - points_per_level - количество очков за уровень
    """
    super().__init__(ComponentsEnum.LEVEL)
    self._stats = stats
    self._max_level = max_level
    self._points = initial_points
    self._point_per_level = points_per_level
    self._current_level = initial_level

  def recieve(self, message:Message):
    if not isinstance(self, message.recipient):
      return
    if message.code == MessageCode.SHOW_CHARACTER_INFO:
      message.addAnswer(self._id, self.getDescription())
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

  def increaseStats(self, stat, value):
    if value > self.points:
      return "Недостаточно очков"
    if stat == StatsEnum.PHYSIQUE:
      self._stats.increasePhysique(value)
      self._points -= value
      return f"Телосложение увеличено на {value}. Текущее значение: {self._stats.physique}"
    if stat == StatsEnum.STRENGTH:
      self._stats.increaseStrength(value)
      self._points -= value
      return f"Сила увеличена на {value}. Текущее значение: {self._stats.strength}"
    if stat == StatsEnum.AGILITY:
      self._stats.increaseAgility(value)
      self._points -= value
      return f"Ловкость увеличена на {value}. Текущее значение: {self._stats.agility}"

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
