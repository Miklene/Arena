from PyQt5.QtWidgets import QWidget
from components.journal_component import JournalComponent
from gui.journal_widget import Ui_JournalWidget

from mvp.game_window.game_window_meta import GameWindowMeta
from mvp.game_window.game_window_view import GameWindowView
from mvp.journal_widget.journal_widget_presenter import JournalWidgetPresenter
from mvp.journal_widget.journal_widget_view import JournalWidgetView


class JournalWidgetLogic(QWidget, JournalWidgetView, metaclass = GameWindowMeta):

    def __init__(self, journal: JournalComponent, parent = None):
        super(JournalWidgetLogic, self).__init__(parent)

        self.ui = Ui_JournalWidget()
        self.ui.setupUi(self)
        self.show()

        self.__parent:GameWindowView = parent
        self.__journal = journal
        self.__presenter = JournalWidgetPresenter(self, self.__journal)
