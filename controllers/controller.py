from abc import ABC, abstractmethod

from views.passive_view import PassiveView

class Controller(ABC):
  def __init__(self, game, model, view = PassiveView()):
    super().__init__()
    self._game = game
    self._model = model
    self._view = view

  @abstractmethod
  def start(self):
    pass  
