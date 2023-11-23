
from abc import ABC, abstractmethod
from observer.observer import Observer
from service_objects import ServiceObjects


class View():
  def __init__(self):
    pass
  
  def display(self, message):
    print(message)
    