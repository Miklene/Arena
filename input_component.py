from abc import ABC, abstractmethod


class InputComponent(ABC):
  def __init__(self):
    pass
  
  @abstractmethod
  def read(self, message):
    pass
    
class ConsoleInputComponent(InputComponent):
  def __init__(self):
    super().__init__()

  def read(self, message):
    return input(message)
    