from PyQt5.QtWidgets import QMainWindow

from gui.game_window.main_window import Ui_MainWindow
from mvp.game_window.game_window_meta import GameWindowMeta
from mvp.game_window.game_window_presenter import GameWindowPresenter
from mvp.game_window.game_window_view import GameWindowView

class GameWindowLogic(QMainWindow, GameWindowView, metaclass = GameWindowMeta):

    def __init__(self, parent = None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.__presenter: GameWindowPresenter = GameWindowPresenter(self)

        self.ui.button_stats.clicked.connect(self.__presenter.button_stats_clicked)
        self.ui.button_abilities.clicked.connect(self.__presenter.button_abilities_clicked)
        self.ui.button_equipment.clicked.connect(self.__presenter.button_equipment_clicked)


    def add_text_to_log(self, text: str) -> None:
        self.ui.log.appendPlainText(text)
