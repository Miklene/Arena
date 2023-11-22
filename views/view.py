
from abc import ABC, abstractmethod
from observer.observer import Observer
from service_objects import ServiceObjects


class View(Observer):
  def __init__(self):
    self._game = ServiceObjects().game
  
  
  @abstractmethod
  def update(self): 
    pass

  def displayMessage(self, message):
    print(message)
    