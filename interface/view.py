from interface.context import IContext
from abc import abstractmethod
from typing import List
from interface.behavior import IBehavior


class IView(object):
    RATE_RATE = 100e-3

    def __init__(self, context: IContext):
        self.context: IContext = context

    @abstractmethod
    def init_view(self):
        pass

    def get_behaviors(self) -> List[IBehavior]:
        return self.context.get_behaviors()

