from abc import abstractmethod
from typing import Tuple


class IEntity(object):

    def __init__(self, uid: int):
        self.uid: int = uid
        self.state: str = ''  # 维护状态

    @abstractmethod
    def get_position(self) -> Tuple[float, float]:
        pass

