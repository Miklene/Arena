from components.component import Component
from message_code import MessageCode

class NameComponent(Component):
  def __init__(self, name):
    self._name = name
  
  def recieve(self, message):
    if not isinstance(self, message.recipient):
      return
    if message == MessageCode.SHOW_DESCRIPTION:
      message.object.out(self._name)
