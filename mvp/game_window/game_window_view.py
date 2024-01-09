from abc import ABCMeta, abstractmethod


class GameWindowView(metaclass = ABCMeta):

    @abstractmethod
    def add_text_to_log(self, text: str) -> None:
        pass
