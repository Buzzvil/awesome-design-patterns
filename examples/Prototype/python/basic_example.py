from __future__ import annotations

from abc import abstractmethod, ABC
from typing import Optional, Dict, Any


class Shape(ABC):
    @abstractmethod
    def clone(self) -> Shape:
        pass

    @classmethod
    @abstractmethod
    def from_shape(cls, shape: Shape) -> Shape:
        pass

    def initialize(self, **kwargs: ...) -> None:
        return


class CommonShape(Shape):
    def __init__(self):
        self.name: str = ''
        self.width: int = 0
        self.height: int = 0

    @classmethod
    def from_shape(cls, shape: Shape) -> Shape:
        new_shape = cls()
        new_shape.name = shape.name
        new_shape.width = shape.width
        new_shape.height = shape.height
        return new_shape

    def clone(self) -> Shape:
        return self.from_shape(self)


class UserDefinedShape(Shape):
    def __init__(self):
        self.name: str = ''
        self.width: int = 0
        self.height: int = 0
        self.memo: str = ''

    @classmethod
    def from_shape(cls, shape: Shape) -> Shape:
        new_shape = cls()
        new_shape.name = shape.name
        new_shape.width = shape.width
        new_shape.height = shape.height
        new_shape.memo = shape.memo
        return new_shape

    def clone(self) -> Shape:
        return self.from_shape(self)

    def initialize(self, **kwargs: ...) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


class Client(ABC):
    @abstractmethod
    def simple_function(self, shape: Shape) -> Dict[str, Any]:
        pass


class ConcreteClient(Client):
    def simple_function(self, shape: Shape) -> Dict[str, Any]:
        clone = shape.clone()
        return dict(name=clone.name, width=clone.width, height=clone.height)


class PickyClient(Client):
    def simple_function(self, shape: Shape) -> Dict[str, Any]:
        shape.initialize(memo='new_memo')
        clone = shape.clone()
        return dict(name=clone.name, width=clone.width, height=clone.height, memo=clone.memo)
