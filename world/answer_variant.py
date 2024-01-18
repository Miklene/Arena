

class AnswerVariant:
    def __init__(self, id: str, text: str, log_text: str = "") -> None:
        self.__id = id
        self.__text = text
        self.__log_text = log_text
        #self.__next_dialog : Dialog = None

    @property
    def text(self) -> str:
        return self.__text

    @property
    def log_text(self) -> str:
        return self.__log_text

    #@property
    #def next_dialog(self) -> Dialog:
    #    return self.__next_dialog

    #@next_dialog.setter
    #def next_dialog(self, next: Dialog) -> None:
    #    self.__next_dialog = next
