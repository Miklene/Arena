from abc import ABC, abstractmethod

class Component(ABC):
  
  @abstractmethod
  def recieve(self, message):
    pass
