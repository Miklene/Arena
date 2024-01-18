

class AnswerVariant:
    def __init__(self, id: str, text: str, next_dialog_id:str, log_text: str = "") -> None:
        self.__id = id
        self.__text = text
        self.__log_text = log_text
        self.__next_dialog_id = next_dialog_id

    @property
    def text(self) -> str:
        return self.__text

    @property
    def log_text(self) -> str:
        return self.__log_text

    @property
    def id(self) -> str:
        return self.__id

    @property
    def next_dialog_id(self) -> str:
        return self.__next_dialog_id

    #@next_dialog.setter
    #def next_dialog(self, next: Dialog) -> None:
    #    self.__next_dialog = next
