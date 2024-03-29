from components.component import Component
from components.components_enum import ComponentsEnum
from messages.message import Message


class Entity:
  """Базовый класс для всех игровых сущностей.

  Является контейнером для компонентов

  Аттрибуты:
  ---------
  components:list[Component]
    список компонентов

  Методы
  ------
  addComponent(component)
    Добавляет компонент в список
  getComponent(component_type)
    Возвращает компонент принятого типа компонента.
    Кидает exception, если такого компонента нет
  send(message)
    Отправляет сообщение всем компонентам
  """

  def __init__(self):
    self._components:list[Component] = []
    self._name = ""

  def addComponent(self, component:Component):
    """Добавить компонент в список"""
    self._components.append(component)


  def getComponent(self, component_type: ComponentsEnum) -> Component:
    """Метод получения компонента по его типу

  Raises
  ------
  ValueError
    Если такого компонента нет, то вызовется исключение
  """
    for component in self._components:
      if component.id == component_type:
        return component
    raise ValueError('No such component')


  def send(self, message:Message):
    for component in self._components:
      component.recieve(message)

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, name):
    self._name = name
