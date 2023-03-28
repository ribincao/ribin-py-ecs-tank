from abc import abstractmethod


class ICommand(object):

    def __init__(self, eid: int):
        self.eid: int = eid

    @abstractmethod
    def execute(self):
        pass

