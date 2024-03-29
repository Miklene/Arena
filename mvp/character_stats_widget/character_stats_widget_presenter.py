from components.components_enum import ComponentsEnum
from components.level_component import LevelComponent
from components.stats_component import FighterStatsComponent
from entities.creature import Creature
from mvp.character_stats_widget.character_stats_widget_view import CharacterStatsWidgetView
from components.stats_component import StatsObserver

class CharacterStatsWidgetPresenter(StatsObserver):
    def __init__(self, view: CharacterStatsWidgetView, player: Creature):
        self.__view = view
        self.__player = player
        self.__stats: FighterStatsComponent = self.__player.getComponent(ComponentsEnum.STATS)

        self.__stats.addObserver(self)

        self.__physique = self.__stats.physique
        self.__strength = self.__stats.strength
        self.__agility = self.__stats.agility

        self.__level: LevelComponent = self.__player.getComponent(ComponentsEnum.LEVEL)
        self.__points = self.__level.points

        if self.__points == 0:
            self.__view.set_button_physique_increase_activity(False)
            self.__view.set_button_strength_increase_activity(False)
            self.__view.set_button_agility_increase_activity(False)

        self.__view.set_button_physique_decrease_activity(False)
        self.__view.set_button_strength_decrease_activity(False)
        self.__view.set_button_agility_decrease_activity(False)

        self.__view.set_label_physique_level_text(str(self.__physique))
        self.__view.set_label_strength_level_text(str(self.__strength))
        self.__view.set_label_agility_level_text(str(self.__agility))

        self.__view.set_label_points_value_text(str(self.__points))


    def update(self):
        self.__physique = self.__stats.physique
        self.__strength = self.__stats.strength
        self.__agility = self.__stats.agility

        self.__view.set_label_physique_level_text(str(self.__physique))
        self.__view.set_label_strength_level_text(str(self.__strength))
        self.__view.set_label_agility_level_text(str(self.__agility))

    def button_physique_increase_clicked(self):
        if self.__points > 0:
            self.__physique += 1
            self.__view.set_button_physique_decrease_activity(True)
            self.__points -= 1
            self.__view.set_label_points_value_text(str(self.__points))
            self.__view.set_label_physique_level_text(str(self.__physique))
        if self.__points == 0:
            self.__set_buttons_increase_activity(False)


    def button_physique_decrease_clicked(self):
        if self.__physique > self.__stats.physique:
            self.__physique -= 1
            self.__points += 1
            self.__view.set_label_points_value_text(str(self.__points))
            self.__view.set_label_physique_level_text(str(self.__physique))
            if self.__physique == self.__stats.physique:
                self.__view.set_button_physique_decrease_activity(False)
        if self.__points > 0:
            self.__set_buttons_increase_activity(True)

    def button_strength_increase_clicked(self):
        if self.__points > 0:
            self.__strength += 1
            self.__view.set_button_strength_decrease_activity(True)
            self.__points -= 1
            self.__view.set_label_points_value_text(str(self.__points))
            self.__view.set_label_strength_level_text(str(self.__strength))
        if self.__points == 0:
            self.__set_buttons_increase_activity(False)

    def button_strength_decrease_clicked(self):
        if self.__strength > self.__stats.strength:
            self.__strength -= 1
            self.__points += 1
            self.__view.set_label_points_value_text(str(self.__points))
            self.__view.set_label_strength_level_text(str(self.__strength))
            if self.__strength == self.__stats.strength:
                self.__view.set_button_strength_decrease_activity(False)
        if self.__points > 0:
            self.__set_buttons_increase_activity(True)

    def button_agility_increase_clicked(self):
        if self.__points > 0:
            self.__agility += 1
            self.__view.set_button_agility_decrease_activity(True)
            self.__points -= 1
            self.__view.set_label_points_value_text(str(self.__points))
            self.__view.set_label_agility_level_text(str(self.__agility))
        if self.__points == 0:
            self.__set_buttons_increase_activity(False)

    def button_agility_decrease_clicked(self):
        if self.__agility > self.__stats.agility:
            self.__agility -= 1
            self.__points += 1
            self.__view.set_label_points_value_text(str(self.__points))
            self.__view.set_label_agility_level_text(str(self.__agility))
            if self.__agility == self.__stats.agility:
                self.__view.set_button_agility_decrease_activity(False)
        if self.__points > 0:
            self.__set_buttons_increase_activity(True)

    def __set_buttons_increase_activity(self, active: bool) -> None:
        self.__view.set_button_physique_increase_activity(active)
        self.__view.set_button_strength_increase_activity(active)
        self.__view.set_button_agility_increase_activity(active)
