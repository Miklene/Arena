from equipment import Equipment, Weapon, Armor
from fighter import Fighter
from output import ConsoleOutputComponent
from stats_requirements import WeaponStatsRequirmentsComponent, ArmorStatsRequirmentsComponent
from components.stats_component import FighterStatsComponent
from screen import NewGameScreen
from input_component import ConsoleInputComponent

class Game:
  def __init__(self):
    self._output = ConsoleOutputComponent()
    self._input = ConsoleInputComponent()
    self._screen = NewGameScreen(self)
    self._player = None
  
  def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Game, cls).__new__(cls)
        return cls.instance

  @property
  def player(self):
    return self._player

  @property
  def output(self):
    return self._output

  @player.setter
  def player(self, player):
    self._player = player

  def start(self):
    self._screen.start(self._output, self._input)
  
  
