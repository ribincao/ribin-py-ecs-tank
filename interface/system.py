from abc import abstractmethod
from interface.entity import IEntity
from typing import List


class ISystem(object):

    def __init__(self):
        self.group: List[IEntity] = []

    @abstractmethod
    def update(self):
        pass

