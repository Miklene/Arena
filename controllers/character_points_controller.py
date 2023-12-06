from contextlib import suppress
from components.components_enum import ComponentsEnum
from components.stats_component import StatsEnum
from controllers.controller import Controller
from screens.screens_enum import ScreensEnum


class CharacterPointsController(Controller):
  def __init__(self, game, model):
    super().__init__(game, model)

  def start(self):
    while True:
      with suppress(ValueError):
        self._view.display(f"Очки умений: {self._model.getComponent(ComponentsEnum.LEVEL).points}")  
        choiсe = input("1 - увеличить телосложение\n2 - увеличить силу\n3 - увеличить ловкость\n4 - подсказка по очкам умений\n0 - назад\n")
        if choiсe == "1":
          points = int(input("Телосложение, введите количество очков:"))
          message = self._model.getComponent(ComponentsEnum.LEVEL).increaseStats(StatsEnum.PHYSIQUE, points)
          self._view.display(message)
        if choiсe == "2":
          points = int(input("Сила, введите количество очков:"))
          message = self._model.getComponent(ComponentsEnum.LEVEL).increaseStats(StatsEnum.STRENGTH, points)
          self._view.display(message)
        if choiсe == "3":
          points = int(input("Ловкость, введите количество очков:"))
          message = self._model.getComponent(ComponentsEnum.LEVEL).increaseStats(StatsEnum.AGILITY, points)
          self._view.display(message)
          #self._game.player.send(UpgradeStatsMessage({"agility" : points}))
        if choiсe == "4":
          self._view.display(self._model.getComponent(ComponentsEnum.PARAMETERS).showParametersPerStats())
        if choiсe == "0":
          self._game.setNextScreen(ScreensEnum.PREVIOUS)
