from abc import ABC, abstractmethod
from fighter import Orc, Elf, Human
from output import ConsoleOutputComponent
from message import DescriptionMessage

class Screen(ABC):
  def __init__(self, game):
    self._game = game
  
  @abstractmethod
  def start(self, output, inp):
    pass
    
class NewGameScreen(Screen):
  def __init__(self, game):
    super().__init__(game)
  
  def start(self, output, inp):
    while True:
      race = inp.read("В игре есть три расы: орк, человек, эльф. Введите:\n1 - орк\n2 - человек\n3 - эльф\n")
      if race == "1":
        output.out("")
        Orc().send(DescriptionMessage(output))
        accept = inp.read("1 - выбрать\n0 - назад\n")
        if accept == "1":
          player = Orc()
          break
      elif race == "2":
        output.out("")
        Human().send(DescriptionMessage(output))
        accept = inp.read("1 - выбрать\n0 - назад\n")
        if accept == "1":
          player = Human()
          break
      elif race == "3":
        output.out("")
        Elf().send(DescriptionMessage(output))
        accept = inp.read("1 - выбрать\n0 - назад\n")
        if accept == "1":
          player = Elf()
          break
    name = inp.read("Введите свое имя: ")
    player.name = name
    self._game.player = player
    output.out(f"Добро пожаловать на арену, {player.race} {player.name}")
    MainMenuScreen(self._game).start(output, inp)


class MainMenuScreen(Screen):
  def __init__(self, game):
    super().__init__(game)

  def start(self, output, inp):
    while True:
      output.out("\nГлавное меню")
      #output.out(f"У вас {str(self._game.player.money)} монет и {str(self._game.player.points)} нераспределенных очков умений")
      choiсe = inp.read("1 - меню персонажа\n2 - меню магазина\n3 - меню боя\n")
      if choiсe == "1":
        CharacterMenuScreen(self._game).start(output, inp)
      #if choiсe == "2":
      #  self.storeMenu()
      #if choiсe == "3":
      #  self.fightMenu()  

class CharacterMenuScreen(Screen):
  def __init__(self, game):
    super().__init__(game)

  def start(self, output, inp):
    while True:
      output.out("\nМеню персонажа")
      #output.out(f"У вас {str(self.player.points)} нераспределенных очков умений")
      choiсe = inp.read("1 - характеристики персонажа\n2 - распределить очки умений\n3 - инвентарь\n0 - назад\n")
      if choiсe == "1":
        output.out("")
        self._game.player.send(DescriptionMessage(output))
      #elif choiсe == "2":
      #  self.pointsMenu()
      #elif choiсe == "3":
      #  self.player.inventoryMenu()
      elif choiсe == "0":
        break
