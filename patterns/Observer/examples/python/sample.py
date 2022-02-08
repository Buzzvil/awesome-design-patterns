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
    def get_state(self) -> str:
        pass


NONE_STATE = ''


class PhoneStore(Subject):
    state: str
    _observers: List[Observer]

    def __init__(self) -> None:
        self.state = NONE_STATE
        self._observers = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def update_state(self, new_state: str) -> None:
        self.state = new_state
        self.notify()

    def get_state(self) -> str:
        return self.state


class Observer(ABC):
    last_notified_state: str = NONE_STATE

    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class IPhoneObserver(Observer):
    def __init__(self) -> None:
        self.last_notified_state = NONE_STATE

    def update(self, subject: Subject) -> None:
        if "IPhone" in subject.get_state():
            self.last_notified_state = subject.get_state()


class GalaxyObserver(Observer):
    def __init__(self) -> None:
        self.last_notified_state = NONE_STATE

    def update(self, subject: Subject) -> None:
        if "Galaxy" in subject.get_state():
            self.last_notified_state = subject.get_state()
