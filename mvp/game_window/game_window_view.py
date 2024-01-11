from abc import ABCMeta, abstractmethod


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
