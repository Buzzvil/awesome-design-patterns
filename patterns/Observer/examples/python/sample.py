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


class PhoneStore(Subject):
    state: str = None
    _observers: List[Observer] = []

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


NOT_OBSERVED = ''


class Observer(ABC):
    last_notified_state: str = NOT_OBSERVED

    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class IPhoneObserver(Observer):
    def update(self, subject: Subject) -> None:
        if "IPhone" in subject.get_state():
            self.last_notified_state = subject.get_state()


class GalaxyObserver(Observer):
    def update(self, subject: Subject) -> None:
        if "Galaxy" in subject.get_state():
            self.last_notified_state = subject.get_state()
