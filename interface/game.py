from abc import abstractmethod


class IGame(object):

    def __init__(self, gid: int):
        self.gid: int = gid

    @abstractmethod
    def update(self):
        pass
