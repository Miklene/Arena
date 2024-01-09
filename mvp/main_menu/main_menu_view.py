from abc import ABCMeta, abstractmethod
from PyQt5.QtWidgets import *

class MainMenuView(metaclass = ABCMeta):

    @abstractmethod
    def set_button_back_visibility(self, visible:bool)->None:
        pass

    @abstractmethod
    def start_new_game(self)->None:
        pass
