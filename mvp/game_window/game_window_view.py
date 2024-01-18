from abc import ABCMeta, abstractmethod

from components.inventory_component import InventoryComponent
from entities.creature import Creature
from world.location import Location


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
    def add_variant(self, variant: str, id: str) -> None:
        pass

    @abstractmethod
    def show_inventory(self, inventory: InventoryComponent) -> None:
        pass

    @abstractmethod
    def hide_inventory(self) -> None:
        pass

    @abstractmethod
    def show_stats(self, player: Creature) -> None:
        pass

    @abstractmethod
    def hide_stats(self) -> None:
        pass

    @abstractmethod
    def set_locations_to_list(self, locations: list[Location]) -> None:
        pass

    @abstractmethod
    def set_persons_to_list(self, persons) -> None:
        pass
