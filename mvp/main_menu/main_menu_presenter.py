from mvp.main_menu.main_menu_view import MainMenuView


class MainMenuPresenter:

    def __init__(self, view: MainMenuView) -> None:
        self.__view = view

    def button_new_game_clicked(self):
        self.__view.show_new_game_menu()
