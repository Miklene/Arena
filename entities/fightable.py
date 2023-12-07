from abc import ABC, abstractmethod
class Fightable(ABC):
  def __init__(self) -> None:
    super().__init__()
  
  def joinBattle(self, opponent):
    self._opponent = opponent
    self._last_attack_time = 0

  def update(self, delta, pause):
    if (delta - self._last_attack_time) > self._attack_speed:
      pass


  
