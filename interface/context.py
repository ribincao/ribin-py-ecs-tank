from interface.behavior import IBehavior
from interface.entity import IEntity
from typing import List


class IContext(object):

    def __init__(self):
        pass

    def get_behaviors(self) -> List[IBehavior]:
        return []

    def get_entities(self) -> List[IEntity]:
        return []
