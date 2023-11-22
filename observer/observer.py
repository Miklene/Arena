from abc import ABC, abstractmethod
from contextlib import suppress
class Observer(ABC):
  def __init__(self):
    pass

  @abstractmethod
  def update(self): 
    pass

class Observable:
  def __init__(self):
    self._observers = []
    
  def addObserver(self, observer):
    self._observers.append(observer)
    observer.update()
  
  def notifyUpdate(self):
    for observer in self._observers:
      observer.update()
  
  def removeObserver(self, observer):
    with suppress(ValueError):
      self._observers.remove(observer)
