from abc import ABCMeta, abstractmethod

from entities.creature import Creature


class NewGameWidgetView(metaclass=ABCMeta):

    @abstractmethod
    def start_new_game(self, player: Creature) -> None:
        pass
