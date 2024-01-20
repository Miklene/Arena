from abc import ABC, abstractmethod
from components.components_enum import ComponentsEnum
from messages.message import DescriptionMessage, Message, UpgradeStatsMessage, LevelUpMessage


class Component(ABC):

    def __init__(self, id: ComponentsEnum):
        self.__id: ComponentsEnum = id

    @abstractmethod
    def receive(self, message: Message):
        pass

    @property
    def id(self) -> ComponentsEnum:
        return self.__id
