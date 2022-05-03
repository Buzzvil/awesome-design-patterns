# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import List


class Item(object):
    name: str
    price: int

    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price


class DiscountStrategy(ABC):
    @abstractmethod
    def get_discount_amount(self, item: Item) -> int:
        raise NotImplementedError


class CardDiscountStrategy(DiscountStrategy):
    def get_discount_amount(self, item: Item) -> int:
        if item.price <= 10000:
            return int(item.price * 0.2)
        return 2000


class CashDiscountStrategy(DiscountStrategy):
    def get_discount_amount(self, item: Item) -> int:
        return int(item.price * 0.1)


class CheckDiscountStrategy(DiscountStrategy):
    def get_discount_amount(self, item: Item) -> int:
        return 0


class FinalAmountCalculator(object):
    _discount_strategy: DiscountStrategy

    def __init__(self, discount_strategy: DiscountStrategy) -> None:
        self._discount_strategy = discount_strategy

    def set_strategy(self, discount_strategy: DiscountStrategy) -> None:
        self._discount_strategy = discount_strategy

    def calculate_amount(self, items: List[Item]) -> int:
        return sum([item.price - self._discount_strategy.get_discount_amount(item) for item in items])


if __name__ == "__main__":
    items = [Item('keyboard', 30000), Item('mask', 3000), Item('book', 20000)]
    calculator = FinalAmountCalculator(CashDiscountStrategy())
    print(f'Cash : {calculator.calculate_amount(items)}')
    # Cash : 65700

    calculator.set_strategy(CardDiscountStrategy())
    print(f'Card : {calculator.calculate_amount(items)}')
    # Card : 71850

    calculator.set_strategy(CheckDiscountStrategy())
    print(f'Check : {calculator.calculate_amount(items)}')
    # Check: 73000
