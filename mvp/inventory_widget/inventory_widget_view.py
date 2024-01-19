from abc import ABCMeta, abstractmethod
from PyQt5.QtWidgets import QWidget

class InventoryWidgetView(metaclass = ABCMeta):

    @abstractmethod
    def close_widget(self):
        pass

    @abstractmethod
    def add_item_to_tab(self, tab_name: str, widget: QWidget):
        pass
