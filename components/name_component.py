from components.component import Component
from messages.message import Message
from messages.message_code import MessageCode

class NameComponent(Component):
  _name:str

  def __init__(self, name):
    super().__init__("Name")
    self._name = name

  def recieve(self, message:Message):
    if not isinstance(self, message.recipient):
      return
    if message.code == MessageCode.SHOW_CHARACTER_INFO:
      message.addAnswer(id, self._name)
