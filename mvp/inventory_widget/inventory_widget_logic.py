from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5 import QtGui
from components.inventory_component import InventoryComponent
from gui.inventory_widget import Ui_InventoryWidget
from mvp.game_window.game_window_meta import GameWindowMeta
from mvp.game_window.game_window_view import GameWindowView
from mvp.inventory_widget.inventory_widget_presenter import InventoryWidgetPresenter
from mvp.inventory_widget.inventory_widget_view import InventoryWidgetView
from mvp.weapon_widget.weapon_widget_logic import WeaponWidgetLogic


class InventoryWidgetLogic(QWidget, InventoryWidgetView, metaclass = GameWindowMeta):

    def __init__(self, inventory: InventoryComponent, parent = None):
        super(InventoryWidgetLogic, self).__init__(parent)
        self.ui = Ui_InventoryWidget()
        self.ui.setupUi(self)
        self.show()

        self.__parent:GameWindowView = parent

        self.__inventory = inventory

        self.__presenter = InventoryWidgetPresenter(self, self.__inventory)

    def close_widget(self):
        self.__parent.hide_inventory()

    def add_item_to_tab(self, tab_name: str, widget: QWidget):
        if tab_name == 'Weapon':
            item = QListWidgetItem(self.ui.list_widget_weapon)
            item.setSizeHint(widget.sizeHint())
            self.ui.list_widget_weapon.addItem(item)
            self.ui.list_widget_weapon.setItemWidget(item, widget)
        if tab_name == 'Armor':
            item = QListWidgetItem(self.ui.list_widget_armor)
            item.setSizeHint(widget.sizeHint())
            self.ui.list_widget_armor.addItem(item)
            self.ui.list_widget_armor.setItemWidget(item, widget)
