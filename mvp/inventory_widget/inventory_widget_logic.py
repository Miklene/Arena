from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5 import QtGui
from components.inventory_component import InventoryComponent
from gui.inventory_widget import Ui_InventoryWidget
from mvp.game_window.game_window_meta import GameWindowMeta
from mvp.inventory_widget.inventory_widget_view import InventoryWidgetView
from mvp.weapon_widget.weapon_widget_logic import WeaponWidgetLogic


class InventoryWidgetLogic(QWidget, InventoryWidgetView, metaclass = GameWindowMeta):

    def __init__(self, inventory: InventoryComponent, parent = None):
        super(InventoryWidgetLogic, self).__init__(parent)
        self.ui = Ui_InventoryWidget()
        self.ui.setupUi(self)
        self.show()
        self.__inventory = inventory
        sections = self.__inventory.equipment
        for section in sections:
            for i in range(section.len()):
                weaponWidget = WeaponWidgetLogic(section.getEquipmentByIndex(i))
                item = QListWidgetItem(self.ui.listWidget)
                item.setSizeHint(weaponWidget.sizeHint())
                self.ui.listWidget.addItem(item)
                self.ui.listWidget.setItemWidget(item, weaponWidget)
        #self.ui.listWidget.setItemWidget()
