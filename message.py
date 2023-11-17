from message_code import MessageCode
from output import ConsoleOutputComponent


class Message:
  def __init__(self, code):
    self._code = code
    self._object = None

  @property
  def code(self):
    return self._code

  @property
  def object(self):
    return self._object

class DescriptionMessage(Message):
  def __init__(self, output):
    super().__init__(MessageCode.SHOW_DESCRIPTION)
    self._object = output

class UpgradeStatsMessage(Message):
  def __init__(self, output):
    super().__init__(MessageCode.UPGRADE_STATS)
    self._object = output

class LevelUpMessage(Message):
  def __init__(self, output):
    super().__init__(MessageCode.LEVEL_UP)
    self._object = output

class UpdateParameterspMessage(Message):
  def __init__(self, output):
    super().__init__(MessageCode.UPDATE_PARAMETERS)
    self._object = output
