from abc import ABC, abstractmethod



class Fightable(ABC):
  def __init__(self) -> None:
    super().__init__()
  
  @abstractmethod
  def joinBattle(self, opponent):
    pass

  @abstractmethod
  def update(self, delta, pause):
    pass

  @abstractmethod
  def attack(self):
    pass

  @abstractmethod
  def receive_damage(self, damage):
    pass
  
