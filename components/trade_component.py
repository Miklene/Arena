from components.component import Component
from components.components_enum import ComponentsEnum
from screens.equipment import Weapon
from messages.message import Message
from messages.message_code import MessageCode
from service_objects import ServiceObjects



class TradeComponent(Component):
  def __init__(self):
    super().__init__(ComponentsEnum.TRADE)
    self._customer = None
    self._inventory = None
    self._money = 0

  @property
  def inventory(self):
    return self._inventory

  @inventory.setter
  def inventory(self, inventory):
    self._inventory = inventory

  @property
  def customer(self):
    return self._customer

  @customer.setter
  def customer(self, customer):
    self._customer = customer

  @property
  def money(self):
    return self._money

  @money.setter
  def money(self, money):
    self._money = money

  def getInventoryEquipment(self, type):
    #if isinstance(type, Weapon):
      
    return self._inventory.equipment
    
  def recieve(self, message):
    if not isinstance(self, message.recipient):
      return
    if message.code == MessageCode.SHOW_MONEY:
      ServiceObjects().output.out(f"{self._money} монет")
    if message.code == MessageCode.ADD_MONEY:
      self._money += message.object
    if message.code == MessageCode.BEGIN_TRADE:
      self.beginTrade(message.object)
    if message.code == MessageCode.ADD_INVENTORY:
      self.inventory = message.object
      

  def beginTrade(self, customer):
    output = ServiceObjects().output
    while True:
      self.showInventory()
      output.out("У вас:")
      customer.send(Message(MessageCode.SHOW_CHARACTER_INFO, TradeComponent))
      index = ServiceObjects.input.read("Введите номер товара, которое хотите купить.\ns - для продажи своего оружия\n0 - для выхода\n")
      try:
        index = int(index)
        index -= 1
        if index == -1:
          break
        if not self.inventory.isEquipmentExist():
          output.out("Неверный номер товара")
        else:
          weapon = self.inventory.getEquipmentByIndex(index)
          if weapon.stats_requirments.isSatisfyRequirements(customer.stats, output):
            break
          if customer.buy(self, index):
            print("Вы купили: " + weapon.name)
            equip = input("Хотите экипировать?\n1 - да, 0 - нет\n")
            if equip == "1":
              player.equipWeapon(weapon)
              print("Вы экипировали: " + weapon.name)
          else:
            print("Недостаточно монет")
      except ValueError:
        if index == "s":
          while True:
            player.showWeaponInventory()
            print(f"У вас: {player.money} монет")
            index = input("Введите номер оружия, которое хотите продать.\n0 - для выхода\n")
            with suppress(ValueError):
              index = int(index)
              index -= 1
              if index == -1:
                break
              player.sellWeapon(index)

  
  def showInventory(self):
    self._inventory.showEquipment(ServiceObjects().output)

    