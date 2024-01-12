from abc import ABCMeta, abstractmethod


class MainMenuView(metaclass=ABCMeta):

    @abstractmethod
    def set_button_back_visibility(self, visible: bool) -> None:
        pass

    @abstractmethod
    def show_new_game_menu(self) -> None:
        pass

    @abstractmethod
    def start_new_game(self) -> None:
        pass
