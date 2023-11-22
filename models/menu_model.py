from observer.observer import Observable


class MenuModel(Observable):
  def __init__(self, title):
    super().__init__()
    self._title = title
    self._items = []
  
  def addMenuItem(self, item):
    self._items.append(item)
  
  def getNextMenu(self, index):
    for item in self._items:
      if item.id == index:
        return item.next_menu
    raise ValueError("Нет такого пункта меню")

  @property
  def items(self):
    return self._items

  @property
  def title(self):
    return self._title

class MenuItem:
  def __init__(self, id, text, next_menu):
    self._id = id
    self._text = text
    self._next_menu = next_menu

  @property
  def id(self):
    return self._id
  
  @property
  def text(self):
    return self._text
  
  @property 
  def next_menu(self):
    return self._next_menu
