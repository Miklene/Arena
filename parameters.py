class ParametersComponent:
  HP_PER_PHYSIQUE = 30
  DAMAGE_PER_STRENGTH = 2
  SPEED_PER_AGILITY = 0.2
  def __init__(self, stats):
    pass

class FighterParametersComponent(ParametersComponent):
  def __init__(self, stats):
    super().__init__(stats)
    self._hp = stats.physique * self.HP_PER_PHYSIQUE
    self._damage = stats.strength * self.DAMAGE_PER_STRENGTH
    self._agility = stats.aglity * self.SPEED_PER_AGILITY