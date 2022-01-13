# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class GameClass(metaclass=ABCMeta):
    def __init__(self):
        self.hp = 10
        self.mp = 10

    @abstractmethod
    def level_up(self):
        pass

    def print_status(self):
        print('status hp: {} mp: {}'.format(self.hp, self.mp))


class Warrior(GameClass):
    def __init__(self):
        super(Warrior, self).__init__()
        self.hp += 10

    def level_up(self):
        self.hp += 15
        self.mp += 5

    def print_status(self):
        print('Warrior ', end='')
        super(Warrior, self).print_status()


class Mage(GameClass):
    def __init__(self):
        super(Mage, self).__init__()
        self.mp += 10

    def level_up(self):
        self.hp += 5
        self.mp += 15

    def print_status(self):
        print('Mage ', end='')
        super(Mage, self).print_status()


class GameClassFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_class(self):
        pass


class WarriorFactory(metaclass=ABCMeta):
    def create_class(self):
        return Warrior()


class MageFactory(metaclass=ABCMeta):
    def create_class(self):
        return Mage()


if __name__ == "__main__":
    warrior_factory = WarriorFactory()
    warrior = warrior_factory.create_class()
    warrior.print_status()
    mage_factory = MageFactory()
    mage = mage_factory.create_class()
    mage.print_status()

    print('[Level Up]')
    warrior.level_up()
    mage.level_up()

    warrior.print_status()
    mage.print_status()

    # Warrior status hp: 20 mp: 10
    # Mage status hp: 10 mp: 20
    # [Level Up]
    # Warrior status hp: 35 mp: 15
    # Mage status hp: 15 mp: 35
