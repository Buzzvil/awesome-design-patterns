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

    def __init__(self, command_up, command_down, command_left, command_right):
        self.button_up = command_up
        self.button_down = command_down
        self.button_left = command_left
        self.button_right = command_right
        self._command_history = []

    def execute_command(self, command):
        command.execute()
        self._command_history.append(command)

    def button_up_clicked(self):
        self.execute_command(self.button_up)

    def button_down_clicked(self):
        self.execute_command(self.button_down)

    def button_left_clicked(self):
        self.execute_command(self.button_left)

    def button_right_clicked(self):
        self.execute_command(self.button_right)

    def print_history(self):
        print('[' + ', '.join(command.info() for command in self._command_history) + ']')


if __name__ == "__main__":
    light_receiver = LightReceiver()
    heater_receiver = HeaterReceiver()

    remote_controller = RemoteController(
        command_up=TurnOnCommand(light_receiver),
        command_down=TurnOffCommand(light_receiver),
        command_left=TurnOffCommand(heater_receiver),
        command_right=TurnOffCommand(heater_receiver),
    )

    remote_controller.button_up_clicked()
    # Light turn on. It's bright here
    remote_controller.button_down_clicked()
    # Light turn off. It's dark here
    remote_controller.button_left_clicked()
    # Heater turn off. It's getting cold here.
    remote_controller.button_right_clicked()
    # Heater turn off. It's getting cold here.
    remote_controller.print_history()
    # [LightReceiver turn on, LightReceiver turn off, HeaterReceiver turn off, HeaterReceiver turn off]
