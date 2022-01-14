class Coin:
    __instance = None
    __coin = 0

    @classmethod
    def __new__(cls, *args):
      if cls.__instance is None:
        cls.__instance = object.__new__(cls, *args)
      return cls.__instance

    def get_coin(self):
      return self.__coin

    def add_coin(self):
      self.__coin += 10

    def deduct_coin(self):
      self.__coin -= 1