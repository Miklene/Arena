from abc import ABCMeta, abstractmethod


class MainWindowView(metaclass=ABCMeta):

    @abstractmethod
    def show_new_game_menu(self) -> None:
        pass

    @abstractmethod
    def start_new_game(self):
        pass
