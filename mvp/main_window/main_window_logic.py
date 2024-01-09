from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from gui.main_window.main_window import Ui_MainWindow
from mvp.main_menu.main_menu_logic import MainMenuLogic
from mvp.new_game_widget.new_game_widget_logic import NewGameWidgetLogic

class MainWindowLogic(QMainWindow):
    def __init__(self, parent: QWidget = None) -> None:
        super(MainWindowLogic, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__current_widget = None
        self.__setNewWidget(MainMenuLogic(self))

    def start_new_game(self)-> None:
        self.__setNewWidget(NewGameWidgetLogic(self))

    def __setNewWidget(self, widget: QWidget)-> None:
        if self.__current_widget is not None:
            self.ui.verticalLayout_2.removeWidget(self.__current_widget)
            self.ui.setupUi(self)
        self.__current_widget = widget
        self.ui.verticalLayout_2.addWidget(self.__current_widget)
