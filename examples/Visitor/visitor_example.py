from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class Product(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> int:
        ...


class Beverage(Product):
    def accept(self, visitor: Visitor) -> int:
        return visitor.visit_beverage()


class Snack(Product):
    def accept(self, visitor: Visitor) -> int:
        return visitor.visit_snack()


class CompositeProduct(Product):
    def __init__(self):
        self._products: List[Product] = list()

    def add(self, product: Product):
        self._products.append(product)

    def accept(self, visitor: Visitor) -> int:
        s = 0
        for product in self._products:
            s += product.accept(visitor)
        return s


class Visitor(ABC):
    @abstractmethod
    def visit_beverage(self) -> int:
        ...

    @abstractmethod
    def visit_snack(self) -> int:
        ...


class ConcreteVisitor(Visitor):
    def visit_beverage(self):
        return 1500

    def visit_snack(self) -> int:
        return 2000


class App:
    def main(self, p: Product, v: Visitor) -> int:
        return p.accept(v)
