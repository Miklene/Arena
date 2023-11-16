from equipment import Equipment, Weapon, Armor
from fighter import Fighter
from output import ConsoleOutputComponent
from stats_requirements import WeaponStatsRequirmentsComponent, ArmorStatsRequirmentsComponent
from stats import FighterStatsComponent
from screen import NewGameScreen
from input_component import ConsoleInputComponent

class Game:
  def __init__(self):
    self._output = ConsoleOutputComponent()
    self._input = ConsoleInputComponent()
    self._screen = NewGameScreen()
    
  def start(self):
    self._screen.start(self._output, self._input)

