from abc import ABC


class Mediator(ABC):
    def notify(self, sender: object, event: str) -> None:
        pass


class Waiter:
    def __init__(self):
        self.mediator = None

    def set_mediator(self, mediator: Mediator) -> None:
        self.mediator = mediator

    def get_order(self):
        print("Waiter: Doing something for getting order")
        self.mediator.notify(self, "Finish to get order")


class Chef:
    def __init__(self):
        self.mediator = None

    def set_mediator(self, mediator: Mediator) -> None:
        self.mediator = mediator

    def make_dish(self):
        print("Chef: Doing something for making dish")
        self.mediator.notify(self, "Finish to make dish")


class Server:
    def __init__(self):
        self.mediator = None

    def set_mediator(self, mediator: Mediator) -> None:
        self.mediator = mediator

    def serve_dish(self):
        print("Server: Doing something for serving dish")
        self.mediator.notify(self, "Finish to serve dish")


class HeadChef(Mediator):
    def __init__(self, waiter: Waiter, chef: Chef, server: Server):
        self.waiter = waiter
        self.chef = chef
        self.server = server
        self.waiter.set_mediator(self)
        self.chef.set_mediator(self)
        self.server.set_mediator(self)

    def notify(self, sender: object, event: str) -> None:
        if event == "Finish to get order":
            self.chef.make_dish()

        if event == "Finish to make dish":
            self.server.serve_dish()

        if event == "Finish to serve dish":
            print("HeadChef: Serving completed")


if __name__ == '__main__':
    waiter = Waiter()
    chef = Chef()
    server = Server()

    head_chef = HeadChef(waiter, chef, server)

    waiter.get_order()

    ''' 
    output:
    Waiter: Doing something for getting order
    Chef: Doing something for making dish
    Server: Doing something for serving dish
    HeadChef: Serving completed
    '''
