from enum import Enum


class MessageCode(Enum):
  SHOW_CHARACTER_INFO = 1
  UPGRADE_STATS = 2
  LEVEL_UP = 3
  UPDATE_PARAMETERS = 4
  SHOW_PARAMETERS_PER_STATS = 5
  SHOW_POINTS = 6
  SELL_ITEM = 7
  ADD_MONEY = 8
  BEGIN_TRADE = 9
  ADD_INVENTORY = 10
  SHOW_CHARACTER_EQUIPMENT = 11
  SHOW_MONEY = 12
  #Stats
  GET_PHYSIQUE = 100
  GET_STRENGTH = 101
  GET_AGILITY = 102
  #Parameters
  GET_ARMOR = 110
  GET_HP = 111
  GET_CURRENT_HP = 112
