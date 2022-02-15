import pytest
from datetime import datetime
from iterator_example import Car, FILOIterator, MinHeapIterator

def test_FILO_iterator():
    cars = [
        Car(id="First", brand_name="BMW", parked_at=datetime(2022, 1, 25, 3, 0, 0)),
        Car(id="Second", brand_name="Toyota", parked_at=datetime(2022, 1, 25, 2, 0, 0)),
        Car(id="Third", brand_name="Audi", parked_at=datetime(2022, 1, 25, 1, 0, 0)),
        Car(id="Fourth", brand_name="Cadillac", parked_at=datetime(2022, 1, 25, 4, 0, 0)),
    ]
    expected = ["Fourth", "Third", "Second", "First"]

    it = FILOIterator(data=cars)
    for index, item in enumerate(it):
        assert(expected[index] == item.id)


def test_min_heap_iterator():
    cars = [
        Car(id="First", brand_name="BMW", parked_at=datetime(2022, 1, 25, 3, 0, 0)),
        Car(id="Second", brand_name="Toyota", parked_at=datetime(2022, 1, 25, 2, 0, 0)),
        Car(id="Third", brand_name="Audi", parked_at=datetime(2022, 1, 25, 1, 0, 0)),
        Car(id="Fourth", brand_name="Cadillac", parked_at=datetime(2022, 1, 25, 4, 0, 0)),
    ]
    expected = ["Third", "Second", "First", "Fourth"]

    it = MinHeapIterator(data=cars)
    for index, item in enumerate(it):
        assert(expected[index] == item.id)
