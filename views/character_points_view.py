from views.view import View

class CharacterPointsView(View):
  def __init__(self, model):
    super().__init__()
    self._model = model
    self._model.addObserver(self)
