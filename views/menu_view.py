from views.view import View


class MenuView(View):
  def __init__(self, model):
    super().__init__()
    self._model = model
    self._model.addObserver(self)

  def update(self):
    print(self._model.title)
    items = self._model.items
    for item in items:
      print(f"{item.id} - {item.text}")
  
