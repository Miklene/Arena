class Tradable:
  def __init__(self):
    self._money = 0
  
  @property
  def money(self):
    return self._money
  
  def addMoney(self, money):
    self._money += money
