class Quest:
    def __init__(self, id: str, name: str, description: str, reward_exp: int) -> None:
        self.__id = id
        self.__name = name
        self.__description = description
        self.__reward_exp = reward_exp
        self.__log = []

    def add_message_to_log(self, message: str):
        self.__log.append(message)

    @property
    def id(self):
        return self.__id
