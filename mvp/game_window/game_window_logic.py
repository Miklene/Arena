from PyQt5.QtWidgets import *
from entities.creature import Creature
from gui.game_widget import Ui_GameWidget
from mvp.game_window.game_window_meta import GameWindowMeta
from mvp.game_window.game_window_presenter import GameWindowPresenter
from mvp.game_window.game_window_view import GameWindowView

class GameWindowLogic(QWidget, GameWindowView, metaclass = GameWindowMeta):

    def __init__(self, player: Creature, parent = None):
        super(GameWindowLogic, self).__init__(parent)
        self.ui = Ui_GameWidget()
        self.ui.setupUi(self)
        self.show()

        self.__presenter: GameWindowPresenter = GameWindowPresenter(self, player)

        self.ui.button_stats.clicked.connect(self.__presenter.button_stats_clicked)
        self.ui.button_abilities.clicked.connect(self.__presenter.button_abilities_clicked)
        self.ui.button_equipment.clicked.connect(self.__presenter.button_equipment_clicked)


    def add_text_to_log(self, text: str) -> None:
        self.ui.log.appendPlainText(text)
