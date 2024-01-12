from PyQt5.QtWidgets import *
from entities.creature import Creature

from gui.main_window import Ui_MainWindow
from mvp.game_window.game_window_logic import GameWindowLogic
from mvp.main_menu.main_menu_logic import MainMenuLogic
from mvp.main_menu.main_menu_meta import MainMenuMeta
from mvp.main_window.main_window_view import MainWindowView

from mvp.new_game_widget.new_game_widget_logic import NewGameWidgetLogic


class MainWindowLogic(QMainWindow, MainWindowView, metaclass=MainMenuMeta):
    def __init__(self, parent: QWidget = None) -> None:
        super(MainWindowLogic, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__current_widget = None
        self.__set_new_widget(MainMenuLogic(self))

    def show_new_game_menu(self) -> None:
        self.__set_new_widget(NewGameWidgetLogic(self))

    def start_new_game(self, player: Creature):
        self.__set_new_widget(GameWindowLogic(player, self))

    def __set_new_widget(self, widget: QWidget) -> None:
        if self.__current_widget is not None:
            self.ui.verticalLayout_2.removeWidget(self.__current_widget)
            self.ui.setupUi(self)
        self.__current_widget = widget
        self.ui.verticalLayout_2.addWidget(self.__current_widget)
