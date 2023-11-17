from game import Game
from service_objects import ServiceObjects
from input_component import ConsoleInputComponent
from output import ConsoleOutputComponent


service_object = ServiceObjects()
service_object.input = ConsoleInputComponent()
service_object.output = ConsoleOutputComponent()
game = Game()
service_object.game = game
game.start()
