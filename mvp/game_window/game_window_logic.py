from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QModelIndex, Qt, QPoint
from components.inventory_component import InventoryComponent
from entities.creature import Creature
from gui.game_widget import Ui_GameWidget
from mvp.character_stats_widget.character_stats_widget_logic import CharacterStatsWidgetLogic
from mvp.game_window.game_window_meta import GameWindowMeta
from mvp.game_window.game_window_presenter import GameWindowPresenter
from mvp.game_window.game_window_view import GameWindowView
from mvp.inventory_widget.inventory_widget_logic import InventoryWidgetLogic
from mvp.main_window.main_window_view import MainWindowView
from world.location import Location
from world.npc import Npc


class GameWindowLogic(QWidget, GameWindowView, metaclass=GameWindowMeta):

    def __init__(self, player: Creature, parent=None):
        super(GameWindowLogic, self).__init__(parent)
        self.ui = Ui_GameWidget()
        self.ui.setupUi(self)
        self.show()

        self.__parent: MainWindowView = parent

        self.__variants: dict[QPushButton, int] = {}
        self.__locations_list: list[Location] = []
        self.__persons_list: list[Npc] = []

        self.__stats_widget = None
        self.__inventory_widget = None

        self.ui.log.setReadOnly(True)

        self.__presenter: GameWindowPresenter = GameWindowPresenter(view=self, player=player)

        self.ui.button_stats.clicked.connect(self.__presenter.button_stats_clicked)
        self.ui.button_abilities.clicked.connect(self.__presenter.button_abilities_clicked)
        self.ui.button_equipment.clicked.connect(self.__presenter.button_equipment_clicked)
        self.ui.list_locations.itemClicked.connect(self.location_selected_in_list)

        self.ui.list_locations.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.list_locations.customContextMenuRequested.connect(self.locations_menu_requested)

        self.ui.list_persons.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.list_persons.customContextMenuRequested.connect(self.persons_menu_requested)

    def locations_menu_requested(self, pos: QPoint):
        menu = QMenu(self)
        move = QAction("Перейти", self)
        move.triggered.connect(self.move_to_location)
        menu.addAction(move)
        menu.exec_(self.ui.list_locations.mapToGlobal(pos))

    def move_to_location(self):
        row = self.ui.list_locations.currentIndex().row()
        self.__presenter.move_to_location(self.__locations_list[row])

    def persons_menu_requested(self, pos: QPoint):
        menu = QMenu(self)
        talk = QAction("Говорить", self)
        talk.triggered.connect(self.talk_with_person)
        menu.addAction(talk)
        menu.exec_(self.ui.list_persons.mapToGlobal(pos))

    def talk_with_person(self):
        row = self.ui.list_persons.currentIndex().row()
        self.__presenter.talk_with_person(self.__persons_list[row])

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
        button: QPushButton = QPushButton(variant, self)
        button.clicked.connect(self.variant_clicked)
        self.__variants[button] = id
        self.ui.layout_choice_buttons.addWidget(button)

    def variant_clicked(self):
        self.__presenter.variant_clicked(self.__variants.get(self.sender()))

    def show_inventory(self, inventory: InventoryComponent) -> None:
        self.__inventory_widget = InventoryWidgetLogic(inventory, self)
        self.ui.widget_container.addWidget(self.__inventory_widget)

    def hide_inventory(self) -> None:
        if self.__inventory_widget is not None:
            self.__inventory_widget.setParent(None)

    def show_stats(self, player: Creature) -> None:
        self.__stats_widget = CharacterStatsWidgetLogic(player, self)
        self.ui.widget_container.addWidget(self.__stats_widget)

    def hide_stats(self) -> None:
        if self.__stats_widget is not None:
            self.__stats_widget.setParent(None)

    def set_locations_to_list(self, locations: list[Location]) -> None:
        self.__locations_list.clear()
        self.ui.list_locations.clear()
        for location in locations:
            self.__locations_list.append(location)
            self.ui.list_locations.addItem(location.name)

    def set_persons_to_list(self, persons: list[Npc]) -> None:
        self.__persons_list.clear()
        self.ui.list_persons.clear()
        for person in persons:
            self.__persons_list.append(person)
            self.ui.list_persons.addItem(person.name)

    def location_selected_in_list(self, item: QListWidgetItem):
        index: QModelIndex= self.ui.list_locations.indexFromItem(item)
        #id = index.row()
        #self.__presenter.location_clicked(self.__locations_list[id])
