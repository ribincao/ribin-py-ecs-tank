

class Singleton(object):
    _inst = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._inst, cls):
            cls._inst = object.__new__(cls)
        return cls._inst


def singleton_wrapper(cls):
    instance = {}

    def _singleton_wrapper(*args, **kargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kargs)
        return instance[cls]

    return _singleton_wrapper


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(id(s1), id(s2), s1 == s2)

    class Test(Singleton):

        def __init__(self):
            self.test = 0

    t1 = Test()
    t2 = Test()

    print(id(t1), id(t2), t1 == t2)

