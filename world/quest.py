class Quest:
    def __init__(self, id: str, name: str, description: str) -> None:
        self.__id = id
        self.__name = name
        self.__description = description
        self.__log = []

    def add_message_to_log(self, message: str):
        self.__log.append(message)

    @property
    def id(self):
        return self.__id
