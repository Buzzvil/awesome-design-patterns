# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class GameClass(ABC):
    class_name: str
    hp: int
    mp: int

    def __init__(self):
        self.class_name = ''
        self.hp = 10
        self.mp = 10

    def print_status(self) -> None:
        print('{} status hp: {} mp: {}'.format(self.class_name, self.hp, self.mp))

    @abstractmethod
    def level_up(self) -> None:
        pass

    @abstractmethod
    def fight(self) -> None:
        pass


class Warrior(GameClass):

    def __init__(self):
        super(Warrior, self).__init__()
        self.class_name = 'Warrior'
        self.hp += 10

    def level_up(self) -> None:
        self.hp += 15
        self.mp += 5

    def fight(self) -> None:
        print('Brandish a sword!')


class Mage(GameClass):
    def __init__(self):
        super(Mage, self).__init__()
        self.class_name = 'Mage'
        self.mp += 10

    def level_up(self) -> None:
        self.hp += 5
        self.mp += 15

    def fight(self) -> None:
        print('Cast Magic!')


class Archer(GameClass):
    def __init__(self):
        super(Archer, self).__init__()
        self.class_name = 'Archer'
        self.hp += 5
        self.mp += 5

    def level_up(self) -> None:
        self.hp += 10
        self.mp += 10

    def fight(self) -> None:
        print('Shoot an arrow!')


class GameClassFactory(ABC):
    @abstractmethod
    def create_class(self) -> GameClass:
        pass

    def play_game(self) -> None:
        game_class = self.create_class()
        game_class.print_status()
        game_class.fight()
        game_class.level_up()
        game_class.print_status()


class WarriorFactory(GameClassFactory):
    def create_class(self) -> GameClass:
        return Warrior()


class MageFactory(GameClassFactory):
    def create_class(self) -> GameClass:
        return Mage()


class ArcherFactory(GameClassFactory):
    def create_class(self) -> GameClass:
        return Archer()


def game_starter(game_class_factory: GameClassFactory) -> None:
    game_class_factory.play_game()


if __name__ == "__main__":

    # Warrior
    print('You picked Warrior.')
    game_starter(WarriorFactory())
    # Warrior status hp: 20 mp: 10
    # Attack with sword!
    # Warrior status hp: 35 mp: 15

    # Mage
    print('You pick Mage.')
    game_starter(MageFactory())
    # Mage status hp: 10 mp: 20
    # Cast Magic!
    # Mage status hp: 15 mp: 35

    # Archer
    print('You pick Archer.')
    game_starter(ArcherFactory())
    # Archer status hp: 15 mp: 15
    # Shoot an arrow!
    # Archer status hp: 25 mp: 25
