class Entity:
  def __init__(self):
    self._components = []
    self._name = ""
  
  def addComponent(self, component):
    self._components.append(component)

  def send(self, message):
    for component in self._components:
      component.recieve(message)

  @property
  def name(self):
    return self._name
   
  @name.setter
  def name(self, name):
    self._name = name
