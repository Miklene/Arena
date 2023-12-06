class StoreController:
  def __init__(self, trader, customer):
    self._trader = trader
    self._customer = customer
  
  def start(self):
    choiсe = input("1 - оружие\n2 - броня\n0 - назад\n")
    if choiсe == "1":
      self.trader.getInventoryEquipment()
      #self.concreteStoreMenu(self.weapon_store)
      #self.weapon_store.menu(self.player)
      #if choiсe == "2":
        #self.concreteStoreMenu(self.armor_store)
        #self.armor_store.menu(self.player)
    #if choiсe == "0":
    #  break
