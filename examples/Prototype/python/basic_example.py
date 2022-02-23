from abc import abstractmethod, ABC


class Shape(ABC):
    @abstractmethod
    def clone(self):
        pass


class Client(ABC):
    @abstractmethod
    def simple_function(self, shape: Shape):
        pass
