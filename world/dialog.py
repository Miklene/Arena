from enum import Enum
from world.answer_variant import AnswerVariant


class DialogActionType(Enum):
    REWARD = "REWARD",

class DialogAction:
    def __init__(self, type: DialogActionType, text:str, reward_id: str):
        self.__type = type
        self.__text = text
        self.__reward_id = reward_id

    @property
    def type(self) -> DialogActionType:
        return self.__type

    @property
    def text(self) -> str:
        return self.__text

    @property
    def reward_id(self) -> str:
        return self.reward_id



class DialogStatus(Enum):
    NOT_READ = 0,
    READ = 1,


class DialogType(Enum):
    INFO = 0,
    QUEST = 1


class Dialog:
    def __init__(self, id: str, author_id: str, text: str, type: DialogType, status: DialogStatus = DialogStatus.NOT_READ):
        self.__id = id
        self.__author_id = author_id
        self.__text = text
        self.__type = type
        self.__status = status
        self.__variants: list[AnswerVariant] = []
        self.__action = None
        self.__next_dialog_id = ""

    @property
    def text(self) -> str:
        return self.__text

    @property
    def variants(self) -> list[AnswerVariant]:
        return self.__variants

    @variants.setter
    def variants(self, variants: list[AnswerVariant]) -> None:
        self.__variants = variants

    @property
    def id(self) -> str:
        return self.__id

    @property
    def next_dialog_id(self) -> str:
        return self.__next_dialog_id

    @next_dialog_id.setter
    def next_dialog_id(self, id: str) -> None:
        self.__next_dialog_id = id

    @property
    def action(self) -> DialogAction:
        return self.__action

    @action.setter
    def action(self, action: DialogAction) -> None:
        self.__action = action
