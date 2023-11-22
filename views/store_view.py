from message import Message
from message_code import MessageCode
from view import View


class StoreView(View):
  def __init__(self):
    super().__init__()
  
  def update(self, trade_component): 
    print("\nМеню магазина")
    coins = self._game.player.getComponnent("Trade").money
    print(f"У вас: {coins} монет")

  #def start(self, output, inp):
  #  while True:
  #    output.out("\nМеню магазина")
  #    output.out("У вас: ")
  #   self._game.player.send(Message(MessageCode.SHOW_DESCRIPTION, TradeComponent))
  #    choiсe = inp.read("1 - оружие\n2 - броня\n0 - назад\n")
  #    if choiсe == "1":
  #      self._game.trader.send(Message(MessageCode.BEGIN_TRADE, TradeComponent, self._game.player))
  #      #self.concreteStoreMenu(self.weapon_store)
  #      #self.weapon_store.menu(self.player)
  #    #if choiсe == "2":
  #      #self.concreteStoreMenu(self.armor_store)
  #      #self.armor_store.menu(self.player)
  #    if choiсe == "0":
  #     break
