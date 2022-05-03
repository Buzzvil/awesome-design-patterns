# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class TextConverter(ABC):
    @abstractmethod
    def operation(self, input_string: str) -> str:
        raise NotImplementedError()


class TextReverseConverter(TextConverter):
    def operation(self, input_string: str) -> str:
        print('[operation]')
        return input_string[::-1]


class TextTwiceConverter(TextConverter):
    def operation(self, input_string: str) -> str:
        print('[operation]')
        return input_string + input_string


class BaseLogger(TextConverter):
    _component: TextConverter = None

    def __init__(self, component: TextConverter):
        self._component = component

    @abstractmethod
    def operation(self, input_string: str) -> str:
        raise NotImplementedError()


class InputLogger(BaseLogger):
    def operation(self, input_string: str) -> str:
        print(f'[start operation] input string: {input_string}')
        return self._component.operation(input_string)


class ResultLogger(BaseLogger):
    def operation(self, input_string: str) -> str:
        operation_result = self._component.operation(input_string)
        print(f'[finish operation] operation result: {operation_result}')
        return operation_result


if __name__ == "__main__":
    converter = TextReverseConverter()
    converter.operation('I love you 3000')
    # [operation]

    converter = InputLogger(converter)
    converter.operation('I love you 3000')
    # [start operation] input string: I love you 3000
    # [operation]

    converter = ResultLogger(converter)
    converter.operation('I love you 3000')
    # [start operation] input string: I love you 3000
    # [operation]
    # [finish operation] operation result: 0003 uoy evol I

    converter = TextTwiceConverter()
    converter = ResultLogger(converter)
    converter.operation('I love you 3000')
    # [operation]
    # [finish operation] operation result: I love you 3000I love you 3000
