from controllers.controller import Controller


class MenuController(Controller):
  def __init__(self, game, model, view):
    super().__init__(game, model, view)


  def start(self):
    while True:
      choice = input()
      try:
        next = self._model.getNextMenu(choice)
        self._game.setNextScreen(next)
        #self._model = next.create()
        #self._view.setModel(self._model)
        #self._game.controller = 
      except ValueError:
        self._views[0].displayMessage()
