from PyQt5.QtWidgets import *
from gui.weapon_widget import Ui_WeaponWidget
from mvp.main_menu.main_menu_meta import MainMenuMeta
from mvp.weapon_widget.weapon_widget_view import WeaponWidgetView
from screens.equipment import Weapon


class WeaponWidgetLogic(QWidget, WeaponWidgetView, metaclass=MainMenuMeta):
    def __init__(self, weapon: Weapon, parent: QWidget = None) -> None:
        super(WeaponWidgetLogic, self).__init__(parent)
        self.ui = Ui_WeaponWidget()
        self.ui.setupUi(self)

        self.__weapon = weapon
        self.ui.label_weapon_name.setText(self.__weapon.name)
        self.ui.label_damage_value.setText(str(self.__weapon.damage))
        self.ui.label_strength_value.setText(str(self.__weapon.stats_requierments.strength_req))
        self.ui.label_agility_value.setText(str(self.__weapon.stats_requierments.agility_req))
        self.ui.label_price_value.setText(str(self.__weapon.price))
