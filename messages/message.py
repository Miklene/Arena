from components.components_enum import ComponentsEnum
from messages.message_code import MessageCode
from output import ConsoleOutputComponent
from functools import singledispatchmethod

class Message:
  def __init__(self, code : MessageCode, recipient = object, object = None):
    self._code : MessageCode = code
    self._object = object
    self._recipient = recipient
    self._answers : dict[ComponentsEnum, str]={}

  @property
  def answers(self):
    return self._answers

  @singledispatchmethod
  def addAnswer(self, id:ComponentsEnum, answer:str):
    if self._answers.get(id) == None:
      self._answers[id] = answer
    else:
      self._answers[id] += answer

  @addAnswer.register(int)
  def addAnswer(self, id:ComponentsEnum, answer:int):
    if self._answers.get(id) == None:
      self._answers[id] = str(answer)
    else:
      self._answers[id] = str(int(self._answers[id]) +  answer)

  def printAnswers(self):
    for answer in self._answers.values():
      print(answer)

  def getAnswer(self, id:ComponentsEnum):
    return self._answers.get(id)

  @property
  def code(self) -> MessageCode:
    return self._code

  @property
  def object(self):
    return self._object

  @property
  def recipient(self):
    return self._recipient


class DescriptionMessage(Message):
  """Сообщение с кодом SHOW_CHARACTER_INFO.
  output - класс вывода
  recipient - получатель сообщения. object - сообщение для всех"""
  def __init__(self, output, recipient = object):
    super().__init__(MessageCode.SHOW_CHARACTER_INFO, recipient)
    self._object = output

  def printAnswers(self, components:list[ComponentsEnum]):
    """Напечатать ответы на сообщения.
    components - список компонентов, чьи ответы нужно вывести. Порядок важен"""
    for component in components:
      if self._answers.get(component) != None:
        print(self._answers.get(component))


class UpgradeStatsMessage(Message):
  def __init__(self, output, recipient = object):
    super().__init__(MessageCode.UPGRADE_STATS, recipient)
    self._object = output

class LevelUpMessage(Message):
  def __init__(self, output, recipient = object):
    super().__init__(MessageCode.LEVEL_UP, recipient)
    self._object = output

class UpdateParameterspMessage(Message):
  def __init__(self, output, recipient = object):
    super().__init__(MessageCode.UPDATE_PARAMETERS, recipient)
    self._object = output

class GetParametersMessage(Message):
  def __init__(self, code: MessageCode, recipient = object):
    super().__init__(code, recipient)
