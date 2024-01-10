from PyQt5.QtWidgets import *
from entities.creature import Creature
from gui.new_game_widget import Ui_WidgetNewGame
from mvp.character_stats_widget.character_stats_widget_logic import CharacterStatsWidgetLogic
from mvp.main_menu.main_menu_meta import MainMenuMeta
from mvp.main_window.main_window_view import MainWindowView
from mvp.new_game_widget.new_game_widget_presenter import NewGameWidgetPresenter

from mvp.new_game_widget.new_game_widget_view import NewGameWidgetView


class NewGameWidgetLogic(QWidget, NewGameWidgetView, metaclass=MainMenuMeta):

    def __init__(self, parent: QWidget = None) -> None:
        super(NewGameWidgetLogic, self).__init__(parent)
        self.__parent: MainWindowView = parent
        self.ui = Ui_WidgetNewGame()
        self.ui.setupUi(self)

        self.__presenter = NewGameWidgetPresenter(self)

        self.ui.button_create.clicked.connect(self.__presenter.button_create_clicked)
        self.ui.line_edit_name.textChanged.connect(self.__presenter.line_edit_text_changed)

        self.__widget = CharacterStatsWidgetLogic(self)
        self.ui.widget_container.addWidget(self.__widget)

    def start_new_game(self, player: Creature):
        self.__parent.start_new_game(player)

    def receive_signal(self):
        print("signal received")
