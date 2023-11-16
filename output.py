from abc import ABC, abstractmethod


class OutputComponent(ABC):

  @abstractmethod
  def out(self, message):
    pass

class ConsoleOutputComponent(OutputComponent):

  def out(self, message):
    print(message)

class FileOutputComponent(OutputComponent):

  def out(self, message):
   #написать в файл
    pass