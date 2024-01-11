from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QListWidgetItem
from components.inventory_component import InventoryComponent
from gui.inventory_widget import Ui_InventoryWidget
from mvp.game_window.game_window_meta import GameWindowMeta
from mvp.inventory_widget.inventory_widget_view import InventoryWidgetView


class InventoryWidgetLogic(QWidget, InventoryWidgetView, metaclass = GameWindowMeta):

    def __init__(self, inventory: InventoryComponent, parent = None):
        super(InventoryWidgetLogic, self).__init__(parent)
        self.ui = Ui_InventoryWidget()
        self.ui.setupUi(self)
        self.show()
        self.__inventory = inventory
        item = QListWidgetItem()
        #self.ui.listWidget.setItemWidget()
