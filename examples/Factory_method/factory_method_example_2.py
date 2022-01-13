# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from examples.Factory_method.factory_method_example_1 import GameClass, Mage, Warrior


class Archer(GameClass):
    def __init__(self):
        super(Archer, self).__init__()
        self.hp += 5
        self.mp += 5

    def level_up(self):
        self.hp += 10
        self.mp += 10

    def print_status(self):
        print('Archer ', end='')
        super(Archer, self).print_status()


class BaseGameClassFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_class(self, class_name):
        pass

    def make_game(self):
        warrior = self.create_class('warrior')
        mage = self.create_class('mage')
        archer = self.create_class('archer')
        return warrior, mage, archer


class GameClassFactory(BaseGameClassFactory):
    def create_class(self, class_name):
        if class_name == 'mage':
            return Mage()
        elif class_name == 'archer':
            return Archer()
        else:
            return Warrior()


if __name__ == "__main__":
    game_class_factory = GameClassFactory()
    players = game_class_factory.make_game()
    for player in players:
        player.print_status()

    print('[Level Up]')
    for player in players:
        player.level_up()

    for player in players:
        player.print_status()

    # Warrior status hp: 20 mp: 10
    # Mage status hp: 10 mp: 20
    # Archer status hp: 15 mp: 15
    # [Level Up]
    # Warrior status hp: 35 mp: 15
    # Mage status hp: 15 mp: 35
    # Archer status hp: 25 mp: 25
