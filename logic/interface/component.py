

class Component(object):

    def __init__(self):
        pass

    def serialize(self) -> dict:
        return self.__dict__

