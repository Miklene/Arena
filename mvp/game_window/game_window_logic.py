from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
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

        self.__variants: dict[QPushButton, int] = {}

        self.__presenter: GameWindowPresenter = GameWindowPresenter(view=self, player=player)

        self.ui.button_stats.clicked.connect(self.__presenter.button_stats_clicked)
        self.ui.button_abilities.clicked.connect(self.__presenter.button_abilities_clicked)
        self.ui.button_equipment.clicked.connect(self.__presenter.button_equipment_clicked)



    def add_text_to_log(self, text: str) -> None:
        self.ui.log.appendPlainText(text)

    def set_log_text_color(self, text_color) -> None :
        text_char_format = self.ui.log.currentCharFormat()
        text_char_format.setForeground(text_color)
        self.ui.log.setCurrentCharFormat(text_char_format)

    def insert_text_to_log(self, text: str) -> None:
        self.ui.log.insertPlainText(text)

    def clear_variants(self) -> None:
        for i in reversed(range(self.ui.layout_choice_buttons.count())):
            self.ui.layout_choice_buttons.itemAt(i).widget().deleteLater()

    def add_variant(self, variant: str, id: int) -> None:
        button:QPushButton = QPushButton(variant, self)
        button.clicked.connect(self.variant_clicked)
        self.__variants[button] = id
        self.ui.layout_choice_buttons.addWidget(button)

    def variant_clicked(self):
        sender = self.sender()
        id = self.__variants.get(sender)
        self.__presenter.variant_clicked(id)
