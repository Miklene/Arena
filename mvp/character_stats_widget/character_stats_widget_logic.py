from PyQt5.QtWidgets import *
from gui.character_stats import Ui_CharacterStatsWidget
from mvp.character_stats_widget.character_stats_widget_presenter import CharacterStatsWidgetPresenter
from mvp.character_stats_widget.character_stats_widget_view import CharacterStatsWidgetView



from mvp.main_menu.main_menu_meta import MainMenuMeta


class CharacterStatsWidgetLogic(QWidget, CharacterStatsWidgetView, metaclass = MainMenuMeta):

    def __init__(self, parent: QWidget = None) -> None:
        super(CharacterStatsWidgetLogic, self).__init__(parent)
        self.__parent = parent
        self.ui = Ui_CharacterStatsWidget()
        self.ui.setupUi(self)

        self.__presenter = CharacterStatsWidgetPresenter(self)

        self.ui.button_physique_increase.clicked.connect(self.__presenter.button_physique_increase_clicked)
        self.ui.button_physique_decrease.clicked.connect(self.__presenter.button_physique_decrease_clicked)
        self.ui.button_strength_increase.clicked.connect(self.__presenter.button_strength_increase_clicked)
        self.ui.button_strength_decrease.clicked.connect(self.__presenter.button_strength_decrease_clicked)
        self.ui.button_agility_increase.clicked.connect(self.__presenter.button_agility_increase_clicked)
        self.ui.button_agility_decrease.clicked.connect(self.__presenter.button_agility_decrease_clicked)

    def set_button_physique_increase_activity(self, active: bool) -> None:
        self.ui.button_physique_increase.setEnabled(active)

    def set_button_physique_decrease_activity(self, active: bool) -> None:
        self.ui.button_physique_decrease.setEnabled(active)

    def set_button_strength_increase_activity(self, active: bool) -> None:
        self.ui.button_strength_increase.setEnabled(active)

    def set_button_strength_decrease_activity(self, active: bool) -> None:
        self.ui.button_strength_decrease.setEnabled(active)

    def set_button_agility_increase_activity(self, active: bool) -> None:
        self.ui.button_agility_increase.setEnabled(active)

    def set_button_agility_decrease_activity(self, active: bool) -> None:
        self.ui.button_agility_decrease.setEnabled(active)

    def set_label_physique_level_text(self, text: str) -> None:
        self.ui.label_physique_level.setText(text)

    def set_label_strength_level_text(self, text: str) -> None:
        self.ui.label_strength_level.setText(text)

    def set_label_agility_level_text(self, text: str) -> None:
        self.ui.label_agility_level.setText(text)

    def set_label_points_value_text(self, text: str) -> None:
        self.ui.label_points_value.setText(text)
