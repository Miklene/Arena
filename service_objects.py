class ServiceObjects:
  def __init__(self):
    pass
  
  def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ServiceObjects, cls).__new__(cls)
        return cls.instance

  @property
  def output(self):
    return self._output
  
  @property
  def input(self):
    return self._input
  
  @property 
  def game(self):
    return self._game

  @output.setter
  def output(self, output):
    self._output = output
  
  @input.setter
  def input(self, input):
    self._input = input

  @game.setter
  def game(self, game):
    self._game = game
