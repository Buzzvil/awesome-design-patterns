class SingletonInstance:
    __instance = None

    @classmethod
    def __getInstance(cls):
      return cls.__instance
    
    @classmethod
    def instance(cls, *args, **kwargs):
      cls.__instance = cls(*args, **kwargs)
      cls.instance = cls.__getInstance
      return cls.__instance

class Coin(SingletonInstance):
  def __init__(self):
    self.__coin = 0

  def add_coin(self):
    self.__coin += 10

  def deduct_coin(self):
    self.__coin -= 1

  def get_coin(self):
    return self.__coin
