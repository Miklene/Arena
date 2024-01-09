from mvp.main_menu.main_menu_view import MainMenuView
from mvp.new_game_widget.new_game_widget_logic import NewGameWidgetLogic


class MainMenuPresenter:
    def __init__(self, view:MainMenuView) -> None:
        self.__view = view

    def button_new_game_clicked(self):
        self.__view.start_new_game()
