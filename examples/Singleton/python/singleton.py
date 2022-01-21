class Singleton(type):
    __instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance


class Logger(metaclass=Singleton):
    pass
