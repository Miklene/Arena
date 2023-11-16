from abc import ABC, abstractmethod
from fighter import Orc, Elf, Human


class Screen(ABC):
  def __init__(self):
    pass
  
  @abstractmethod
  def start(self, output, inp):
    pass
    
class NewGameScreen(Screen):
  def __init__(self):
    super().__init__()
  
  def start(self, output, inp):
    while True:
      race = inp.read("В игре есть три расы: орк, человек, эльф. Введите:\n1 - орк\n2 - человек\n3 - эльф\n")
      if race == "1":
        output.out(Orc().getDescription())
        accept = inp.read("1 - выбрать\n0 - назад\n")
        if accept == "1":
          self.player = Orc()
          break
      elif race == "2":
        output.out(Human().getDescription())
        accept = inp.read("1 - выбрать\n0 - назад\n")
        if accept == "1":
          self.player = Human()
          break
      elif race == "3":
        output.out(Elf().getDescription())
        accept = inp.read("1 - выбрать\n0 - назад\n")
        if accept == "1":
          self.player = Elf()
          break
    name = inp.read("Введите свое имя: ")
    self.player.name = name
    output.out(f"Добро пожаловать на арену, {self.player.race} {self.player.name}")