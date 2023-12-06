from abc import ABC, abstractmethod
from components.components_enum import ComponentsEnum
from messages.message import DescriptionMessage, Message, UpgradeStatsMessage, LevelUpMessage


class Component(ABC):
  _id:ComponentsEnum

  def __init__(self, id:ComponentsEnum):
    self._id = id

  @abstractmethod
  def recieve(self, message:Message):
    pass

  @property
  def id(self)->ComponentsEnum:
    return self._id
