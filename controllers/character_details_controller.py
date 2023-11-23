from controllers.controller import Controller
from views.passive_view import PassiveView
from screens_enum import ScreensEnum
from components.components_enum import ComponentsEnum

class CharacterDetailsController(Controller):
  def __init__(self, game, model):
    super().__init__(game, model)
  
  def start(self):
    self._view.display(f"{self._model.race} {self._model.name}")
    self._view.display(self._model.getComponent(ComponentsEnum.LEVEL).getDescription())
    self._view.display(self._model.getComponent(ComponentsEnum.STATS).getDescription())
    self._view.display(self._model.getComponent(ComponentsEnum.PARAMETERS).getDescription())
    self._game.setNextScreen(ScreensEnum.PREVIOUS)
