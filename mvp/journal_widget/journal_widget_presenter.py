from components.journal_component import JournalComponent
from mvp.journal_widget.journal_widget_view import JournalWidgetView


class JournalWidgetPresenter:

    def __init__(self, view: JournalWidgetView, journal: JournalComponent) -> None:
        self.__view = view
        self.__journal = journal
        self.__display_all_quests()

    def __display_all_quests(self):
        quests = self.__journal.quests
        for quest in quests:
            self.__view.add_quest_to_list(quest)
