from abc import ABCMeta, abstractmethod


class NewGameWidgetView(metaclass=ABCMeta):

    @abstractmethod
    def start_new_game(self) -> None:
        pass
