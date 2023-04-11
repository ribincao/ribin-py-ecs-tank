

class Component(object):

    def __init__(self):
        pass

    @property
    def name(self) -> str:
        return self.__class__.__name__[:-9].lower()

    def serialize(self) -> dict:
        return self.__dict__

