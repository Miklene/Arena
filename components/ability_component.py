from components.component import Component
from components.components_enum import ComponentsEnum
from entities.creature import Creature
from messages.message import GetParametersMessage, Message
from messages.message_code import MessageCode
from service_objects import ServiceObjects


class AbilityComponent(Component):
    def __init__(self):
        super().__init__(ComponentsEnum.ABILITY)
        self._player: Creature = ServiceObjects().game.player


class ThickSkin(AbilityComponent):
    """Способоность "Толстая кожа". Дает 1 ед. брони за каждые 100 хп"""

    def __init__(self):
        super().__init__()

    def receive(self, message: Message):
        if message.code == MessageCode.GET_ARMOR:
            hp_mes = GetParametersMessage(MessageCode.GET_HP)
            self._player.send(hp_mes)
            try:
                hp: int = int(hp_mes.getAnswer(ComponentsEnum.HP))
            except ValueError:
                hp: int = 0
            message.addAnswer(ComponentsEnum.ARMOR, int(hp / 100))


class OrcsBlood(AbilityComponent):
    """Способность "Кровь орков". Дает 2 ед хп за каждую единицу телосложения"""

    def __init__(self):
        super().__init__()

    def receive(self, message: Message):
        if message.code == MessageCode.GET_HP:
            phys_mes = GetParametersMessage(MessageCode.GET_PHYSIQUE)
            self._player.send(phys_mes)
            try:
                phys: int = int(phys_mes.getAnswer(ComponentsEnum.PHYSIQUE))
            except:
                phys: int = 0
            message.addAnswer(ComponentsEnum.HP, int(phys * 2))
