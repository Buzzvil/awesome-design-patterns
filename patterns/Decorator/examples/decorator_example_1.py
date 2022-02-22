# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self):
        raise NotImplementedError()


class ConcreteComponent(Component):
    def operation(self):
        print('crawling')


class BaseLogger(Component):
    _component: Component = None

    def __init__(self, component: Component):
        self._component = component

    @abstractmethod
    def operation(self):
        raise NotImplementedError()


class StartLogger(BaseLogger):
    def operation(self):
        print('start operation')
        self._component.operation()


class FinishLogger(BaseLogger):
    def operation(self):
        self._component.operation()
        print('end operation')


if __name__ == "__main__":
    component = ConcreteComponent()
    component.operation()
    # in operation

    component = StartLogger(component)
    component.operation()
    # start operation
    # in operation

    component = FinishLogger(component)
    component.operation()
    # start operation
    # in operation
    # end operation
