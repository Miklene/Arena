from views.view import View


class LevelView(View):
  def __init__(self, model):
    super().__init__()
    self._model = model
    self._model.addObserver(self)
  
  def update(self):
    print(self._model.getDescription())