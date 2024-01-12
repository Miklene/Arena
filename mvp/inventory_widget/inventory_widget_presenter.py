from components.inventory_component import InventoryComponent
from mvp.inventory_widget.inventory_widget_view import InventoryWidgetView
from mvp.weapon_widget.weapon_widget_logic import WeaponWidgetLogic


class InventoryWidgetPresenter:

    def __init__(self, view, inventory: InventoryComponent):
        self.__view: InventoryWidgetView = view
        self.__inventory = inventory
        self.fill_view()

    def fill_view(self):
        sections = self.__inventory.equipment
        for section in sections:
            for i in range(section.len()):
                self.__view.add_item_to_tab(section.name, WeaponWidgetLogic(section.getEquipmentByIndex(i)))

    def button_close_pressed(self):
        self.__view.close_widget()
