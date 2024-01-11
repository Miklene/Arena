from abc import ABCMeta, abstractmethod

from components.inventory_component import InventoryComponent


class GameWindowView(metaclass = ABCMeta):

    @abstractmethod
    def add_text_to_log(self, text: str) -> None:
        pass

    @abstractmethod
    def insert_text_to_log(self, text: str) -> None:
        pass

    def set_log_text_color(self, text_color) -> None :
        pass

    @abstractmethod
    def clear_variants(self) -> None:
        pass

    @abstractmethod
    def add_variant(self, variant: str, id: int) -> None:
        pass

    @abstractmethod
    def show_inventory(self, inventory: InventoryComponent) -> None:
        pass
