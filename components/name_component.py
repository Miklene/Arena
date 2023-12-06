from components.component import Component
from messages.message_code import MessageCode

class NameComponent(Component):
  def __init__(self, name):
    super().__init__("Name")
    self._name = name
  
  def recieve(self, message):
    if not isinstance(self, message.recipient):
      return
    if message == MessageCode.SHOW_CHARACTER_INFO:
      message.object.out(self._name)
