# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import List


class Receiver(ABC):
    @abstractmethod
    def turn_on(self):
        raise NotImplementedError()

    @abstractmethod
    def turn_off(self):
        raise NotImplementedError()

    @abstractmethod
    def info(self):
        raise NotImplementedError()


class LightReceiver(Receiver):
    def turn_on(self):
        print("Light turn on. It's bright here")

    def turn_off(self):
        print("Light turn off. It's dark here")

    def info(self):
        return "LightReceiver"


class HeaterReceiver(Receiver):
    def turn_on(self):
        print("Heater turn on. It's getting warmer here.")

    def turn_off(self):
        print("Heater turn off. It's getting cold here.")

    def info(self):
        return "HeaterReceiver"


class Command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError()

    @abstractmethod
    def info(self):
        raise NotImplementedError()


class TurnOnCommand(Command):
    def __init__(self, receiver: Receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.turn_on()

    def info(self):
        return self._receiver.info() + " turn on"


class TurnOffCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.turn_off()

    def info(self):
        return self._receiver.info() + " turn off"


class RemoteController(object):
    _command_history: List[Command]

    def __init__(self, light_turn_on, light_turn_off, heater_turn_on, heater_turn_off):
        self.light_turn_on = self.execute_command(light_turn_on)
        self.light_turn_off = self.execute_command(light_turn_off)
        self.heater_turn_on = self.execute_command(heater_turn_on)
        self.heater_turn_off = self.execute_command(heater_turn_off)
        self._command_history = []

    def execute_command(self, command):
        def func():
            command.execute()
            self._command_history.append(command)
        return func

    def light_on(self):
        self.light_turn_on()

    def light_off(self):
        self.light_turn_off()

    def heater_on(self):
        self.heater_turn_on()

    def heater_off(self):
        self.heater_turn_off()

    def print_history(self):
        print('[' + ', '.join(command.info() for command in self._command_history) + ']')


if __name__ == "__main__":
    light_receiver = LightReceiver()
    heater_receiver = HeaterReceiver()
    remote_controller = RemoteController(
        light_turn_on=TurnOnCommand(light_receiver),
        light_turn_off=TurnOffCommand(light_receiver),
        heater_turn_on=TurnOffCommand(heater_receiver),
        heater_turn_off=TurnOffCommand(heater_receiver),
    )
    remote_controller.light_on()
    remote_controller.light_off()
    remote_controller.heater_on()
    remote_controller.heater_off()
    remote_controller.print_history()
