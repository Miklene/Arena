from contextlib import suppress
from controllers.controller import Controller
from views.passive_view import PassiveView

class MenuController(Controller):
  def __init__(self, game, model):
    super().__init__(game, model)


  def start(self):
    while True:
      self._view.display(self._model.title)
      items = self._model.items
      for item in items:
        self._view.display(f"{item.id} - {item.text}")
      choice = input()
      with suppress(ValueError):
        next = self._model.getNextMenu(choice)
        self._game.setNextScreen(next)
        #self._model = next.create()
        #self._view.setModel(self._model)
        #self._game.controller = 
  
