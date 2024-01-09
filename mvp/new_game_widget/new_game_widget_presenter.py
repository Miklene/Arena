from mvp.new_game_widget.new_game_widget_view import NewGameWidgetView


class NewGameWidgetPresenter:
    def __init__(self, view:NewGameWidgetView) -> None:
        self.__view = view
        self.__player_name: str = ""

    def button_create_clicked(self):
        pass

    def line_edit_text_changed(self, text: str)-> None:
        self.__player_name = text
