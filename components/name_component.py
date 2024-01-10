from components.component import Component
from messages.message import Message
from messages.message_code import MessageCode
from components.components_enum import ComponentsEnum


class NameComponent(Component):
  """Компонент имени персонажа"""
  def __init__(self, name: str):
    """Инициализация компонента имя
      - name - имя персонажа"""
    super().__init__(ComponentsEnum.NAME)
    self._name = name

  def recieve(self, message:Message):
    if not isinstance(self, message.recipient):
      return
    if message.code == MessageCode.SHOW_CHARACTER_INFO:
      message.addAnswer(id, self._name)
