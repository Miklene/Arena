from abc import ABCMeta, abstractmethod


class JournalWidgetView(metaclass=ABCMeta):

    @abstractmethod
    def add_quest_to_list(self, quest):
        pass

