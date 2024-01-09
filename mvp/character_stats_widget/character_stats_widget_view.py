from abc import ABCMeta, abstractmethod
from PyQt5.QtWidgets import *

class CharacterStatsWidgetView(metaclass = ABCMeta):

    @abstractmethod
    def set_button_physique_increase_activity(self, active: bool) -> None:
        pass

    @abstractmethod
    def set_button_physique_decrease_activity(self, active: bool) -> None:
        pass

    @abstractmethod
    def set_button_strength_increase_activity(self, active: bool) -> None:
        pass

    @abstractmethod
    def set_button_strength_decrease_activity(self, active: bool) -> None:
        pass

    @abstractmethod
    def set_button_agility_increase_activity(self, active: bool) -> None:
        pass

    @abstractmethod
    def set_button_agility_decrease_activity(self, active: bool) -> None:
        pass

    @abstractmethod
    def set_label_physique_level_text(self, text: str) -> None:
        pass

    @abstractmethod
    def set_label_strength_level_text(self, text: str) -> None:
        pass

    @abstractmethod
    def set_label_agility_level_text(self, text: str) -> None:
        pass

    @abstractmethod
    def set_label_points_value_text(self, text: str) -> None:
        pass
