from enum import Enum
from world.answer_variant import AnswerVariant




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

    @property
    def text(self) -> str:
        return self.__text

    @property
    def variants(self) -> list[AnswerVariant]:
        return self.__variants

    @variants.setter
    def variants(self, variants: list[AnswerVariant]) -> None:
        self.__variants = variants
