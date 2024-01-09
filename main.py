
from mvp.main_window.main_window_logic import MainWindowLogic
from service_objects import ServiceObjects
from input_component import ConsoleInputComponent
from output import ConsoleOutputComponent
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindowLogic()
main_window.show()
sys.exit(app.exec_())
#service_object = ServiceObjects()
#service_object.input = ConsoleInputComponent()
#service_object.output = ConsoleOutputComponent()
#game = Game()
#service_object.game = game
#game.start()
