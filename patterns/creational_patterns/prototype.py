# Prototype (Прототип) - порождающий паттерн
# Позволяет копировать объекты, не вдаваясь в подробности их реализации.
#
# Прототип поручает создание копий самим копируемым объектам. Он вводит общий интерфейс для всех объектов,
# поддерживающих клонирование. Это позволяет копировать объекты, не привязываясь к их конкретным классам.
########################################################################################################################
# Применяется:
# - Когда нужно скопировать объект, так чтобы новая копия не ссылалась на атрибуты исходного объекта.
########################################################################################################################
# Плюсы:
# - Позволяет клонировать объекты, не привязываясь к их конкретным классам.
# - Меньше повторяющегося кода инициализации объектов.
# - Ускоряет создание объектов.
# - Альтернатива созданию подклассов для конструирования сложных объектов.
########################################################################################################################
# Минусы:
# - Сложно клонировать составные объекты, имеющие ссылки на другие объекты.
########################################################################################################################
import copy
import datetime
import time
from abc import ABC


class Person(ABC):
    """Прототип создания персонажа"""

    def __init__(self):
        time.sleep(2)  # для визуализации скорости создания новых персонажей
        self.height = None
        self.age = None
        self.defense = None
        self.attack = None

    def clone(self):
        """Метод клонирования"""
        return copy.deepcopy(self)


class Warrior(Person):

    def __init__(self, height, age, defense, attack):
        super().__init__()
        time.sleep(2)  # для визуализации скорости создания новых персонажей
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        self.strength = 60  # дополнительный атрибут класса


class Thief(Person):

    def __init__(self, height, age, defense, attack):
        super().__init__()
        time.sleep(2)  # для визуализации скорости создания новых персонажей
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        self.dexterity = 30  # дополнительный атрибут класса


class Mage(Person):

    def __init__(self, height, age, defense, attack):
        super().__init__()
        time.sleep(2)  # для визуализации скорости создания новых персонажей
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        self.intelligence = 100  # дополнительный атрибут класса


if __name__ == '__main__':
    # ****************************** Creation of 1 character ~ 4 sec ******************************

    print('Starting to create a warrior NPC: ', datetime.datetime.now().time())
    warrior = Warrior(180, 22, 5, 8)
    print('Finished creating a warrior NPC: ', datetime.datetime.now().time())
    print(f'Warrior: {warrior}. Attributes: ' + ', '.join("%s: %s" % item for item in vars(warrior).items()))

    # ******************** Creation of a guild of 5 characters (no copy) ~ 21 sec *******************

    print('Instantiating warriors guild at: ', datetime.datetime.now().time())
    for i in range(5):
        warrior = Warrior(180, 22, 5, 8)
        print(f'Warrior # {i+1}: {warrior}. '
              f'Attributes: ' + ', '.join("%s: %s" % item for item in vars(warrior).items()))
        print(f'Finished creating a warrior NPC {i} at: ', datetime.datetime.now().time())
    print('Finished instantiating warriors guild at: ', datetime.datetime.now().time())

    # ******************* Creation of a guild of 5 characters (with copy) ~ 4 sec ******************

    print('Instantiating warriors guild at: ', datetime.datetime.now().time())
    warrior_template = Warrior(180, 22, 5, 8)
    for i in range(5):
        warrior_clone = warrior_template.clone()
        print(f'Warrior # {i+1}: {warrior_clone}. '
              f'Attributes: ' + ', '.join("%s: %s" % item for item in vars(warrior_clone).items()))
        print(f'Finished creating a warrior clone {i+1} at: ', datetime.datetime.now().time())
    print('Finished instantiating warriors guild at: ', datetime.datetime.now().time())

    # ******************* Creation of 1000 different characters (with copy) ~ 12 sec *****************

    print('Instantiating 1000 NPCs: ', datetime.datetime.now().time())
    warrior_template = Warrior(185, 22, 4, 21)
    thief_template = Thief(180, 22, 5, 8)
    mage_template = Mage(172, 65, 8, 15)
    for i in range(333):
        warrior_clone = warrior_template.clone()
        thief_clone = thief_template.clone()
        mage_clone = mage_template.clone()
        print(f'Finished creating NPC trio clone {i+1} at: ', datetime.datetime.now().time())
    print('Finished instantiating NPC population at: ', datetime.datetime.now().time())
