from abc import abstractmethod
from interface.command import ICommand
from interface.context import IContext
from typing import List


class ISystem(object):

    def __init__(self, context: IContext):
        self.context: IContext = context
        self.commands: List[ICommand] = []

    @abstractmethod
    def update(self):
        pass

