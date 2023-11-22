from abc import ABC, abstractmethod
from message import DescriptionMessage, Message, UpgradeStatsMessage, LevelUpMessage


class Component(ABC):
  def __init__(self, id):
    self._id = id

  @abstractmethod
  def recieve(self, message):
    pass

  @property
  def id(self):
    return self._id
