from message_code import MessageCode
from output import ConsoleOutputComponent


class Message:
  def __init__(self, code, recipient = object, object = None):
    self._code = code
    self._object = object
    self._recipient = recipient

  @property
  def code(self):
    return self._code

  @property
  def object(self):
    return self._object

  @property
  def recipient(self):
    return self._recipient


class DescriptionMessage(Message):
  def __init__(self, output, recipient = object):
    super().__init__(MessageCode.SHOW_DESCRIPTION, recipient)
    self._object = output

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
