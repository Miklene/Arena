from abc import ABC, abstractmethod

class Controller(ABC):
  def __init__(self, game, model):
    super().__init__()
    self._game = game
    self._model = model
    self._views = []

  def addView(self, view):
    self._views.append(view)

  @abstractmethod
  def start(self):
    pass  
