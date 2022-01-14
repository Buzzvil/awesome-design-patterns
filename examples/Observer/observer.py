from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

    @abstractmethod
    def get_state(self) -> int:
        pass


class SomeSubject(Subject):
    state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def update_state(self, new_state: int) -> None:
        self.state = new_state
        self.notify()

    def get_state(self) -> int:
        return self.state


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class SomeObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject.get_state() < 3:
            print(f"SomeObserverA: Reacted to the event, state={subject.get_state()}")


class SomeObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject.get_state() >= 2:
            print(f"SomeObserverB: Reacted to the event, state={subject.get_state()}")


if __name__ == "__main__":
    subject = SomeSubject()

    observer_a = SomeObserverA()
    subject.attach(observer_a)

    observer_b = SomeObserverB()
    subject.attach(observer_b)

    subject.update_state(1)
    subject.update_state(2)

    subject.detach(observer_a)

    subject.update_state(3)
