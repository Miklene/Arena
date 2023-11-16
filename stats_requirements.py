from abc import ABC, abstractmethod
from output import OutputComponent

class StatsRequirementsComponent(ABC):

  @abstractmethod
  def isSatisfyRequirements(self, stats, output):
    pass

class WeaponStatsRequirmentsComponent(StatsRequirementsComponent):
  
  def __init__(self, strength_req, agility_req):
    self._strength_req = strength_req
    self._agility_req = agility_req

  def isSatisfyRequirements(self, stats, output):
    require = True
    if stats.strength < self._strength_req:
      require = False
      output.out(f"Недостаточно силы {self._strength_req - stats.strength}")
    if stats.agility < self._agility_req:
      require = False
      output.out(f"Недостаточно ловкости {self._strength_req - stats.strength}")
    return require

class ArmorStatsRequirmentsComponent(StatsRequirementsComponent):

  def __init__(self, physique_req):
    self._physique_req = physique_req

  def isSatisfyRequirements(self, stats, output):
    require = True
    if stats.physique < self._physique_req:
      require = False
      output.out(f"Недостаточно телосложения {self._physique_req - stats.physique}")
    return require