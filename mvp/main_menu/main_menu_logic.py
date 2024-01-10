from PyQt5.QtWidgets import *
from gui.main_menu import Ui_MainMenu
from mvp.main_menu.main_menu_presenter import MainMenuPresenter

from mvp.main_menu.main_menu_view import MainMenuView
from mvp.main_menu.main_menu_meta import MainMenuMeta
from mvp.main_window.main_window_view import MainWindowView


class MainMenuLogic(QWidget, MainMenuView, metaclass=MainMenuMeta):

    def __init__(self, parent: QWidget = None) -> None:
        super(MainMenuLogic, self).__init__(parent)
        self.__parent: MainWindowView = parent
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.__presenter = MainMenuPresenter(self)
        self.ui.button_new_game.clicked.connect(self.__presenter.button_new_game_clicked)
        self.set_button_back_visibility(False)

    def set_button_back_visibility(self, visible: bool) -> None:
        self.ui.button_back.setVisible(visible)

    def show_new_game_menu(self) -> None:
        self.__parent.show_new_game_menu()
