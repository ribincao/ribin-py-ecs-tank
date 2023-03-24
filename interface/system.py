from abc import abstractmethod
from interface.entity import IEntity
from interface.command import ICommand
from typing import List


class ISystem(object):

    def __init__(self):
        self.group: List[IEntity] = []
        self.commands: List[ICommand] = []

    @abstractmethod
    def update(self):
        pass

