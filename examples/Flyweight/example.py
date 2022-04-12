from typing import List


class MissileFactory:
    def __init__(self):
        self.types = {}

    def get(self, missile_type):
        if missile_type in self.types:
            return


class MissileType:
    def __init__(self, type: str, image: str):
        self.type = type
        self.image = image

    def draw(self, x, y):
        self.type.
        print(f"Got missile on {x}, {y}")


class Missile:
    def __init__(self, type: MissileType, image: str):
        self.type = type
        self.image = image

    def draw(self, x, y):
        self.type.draw(x, y)


class GameCanvas:
    missiles: List[Missile]
    missile_factory: MissileFactory

    def __init__(self) -> None:
        self.missiles = []
        self.missile_factory = MissileFactory()

    def add_missile(self, missile_type: str, image: str):
        type = self.missile_factory.get(missile_type)
        self.missiles.append(Missile(type, ))


    def draw(self):


