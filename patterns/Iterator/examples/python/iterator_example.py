from __future__ import annotations

import heapq
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import TypeVar, Iterator


class AbstractIterator(ABC, Iterator):
    def __init__(self, data) -> None:
        self._data = data

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        pass


T = TypeVar("T")


class FILOIterator(AbstractIterator):
    def __init__(self, data):
        super(FILOIterator, self).__init__(data=data)
        self._idx = len(self._data)

    def __next__(self) -> T:
        self._idx -= 1
        if self._idx < 0:
            raise StopIteration
        return self._data[self._idx]


class MinHeapIterator(AbstractIterator):
    def __init__(self, data):
        super(MinHeapIterator, self).__init__(data=data)
        heapq.heapify(self._data)

    def __next__(self) -> T:
        try:
            popped = heapq.heappop(self._data)
        except IndexError:
            raise StopIteration
        return popped


# Example Usecase
@dataclass(frozen=True)
class Car:
    id: str
    brand_name: str
    parked_at: datetime

    def __eq__(self, other: Car):
        return self.parked_at == other.parked_at

    def __lt__(self, other: Car) -> bool:
        return self.parked_at < other.parked_at


def example_usecase():
    cars = [
        Car(id="123ABCD", brand_name="BMW", parked_at=datetime(2022, 1, 25, 3, 0, 0)),
        Car(id="456EFGH", brand_name="Toyota", parked_at=datetime(2022, 1, 25, 2, 0, 0)),
        Car(id="789IJKL", brand_name="Audi", parked_at=datetime(2022, 1, 25, 1, 0, 0)),
        Car(id="LWYRUP", brand_name="Cadillac", parked_at=datetime(2022, 1, 25, 4, 0, 0)),
    ]

    print("in reversed order")
    it = FILOIterator(data=cars)
    for item in it:
        print(item)

    print("by order or parked_at")
    it = MinHeapIterator(data=cars)
    for item in it:
        print(item)


if __name__ == "__main__":
    example_usecase()
    # Expected output
    #
    # in reversed order
    # >> Car(id='LWYRUP', brand_name='Cadillac', parked_at=datetime.datetime(2022, 1, 25, 4, 0))
    # >> Car(id='789IJKL', brand_name='Audi', parked_at=datetime.datetime(2022, 1, 25, 1, 0))
    # >> Car(id='456EFGH', brand_name='Toyota', parked_at=datetime.datetime(2022, 1, 25, 2, 0))
    # >> Car(id='123ABCD', brand_name='BMW', parked_at=datetime.datetime(2022, 1, 25, 3, 0))
    #
    # by order or parked_at
    # >> Car(id='789IJKL', brand_name='Audi', parked_at=datetime.datetime(2022, 1, 25, 1, 0))
    # >> Car(id='456EFGH', brand_name='Toyota', parked_at=datetime.datetime(2022, 1, 25, 2, 0))
    # >> Car(id='123ABCD', brand_name='BMW', parked_at=datetime.datetime(2022, 1, 25, 3, 0))
    # >> Car(id='LWYRUP', brand_name='Cadillac', parked_at=datetime.datetime(2022, 1, 25, 4, 0))
