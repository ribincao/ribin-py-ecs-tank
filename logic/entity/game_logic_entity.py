from interface.entity import IEntity
from typing import Tuple


class GameLogicEntity(IEntity):

    def __init__(self, uid: int):
        super(GameLogicEntity, self).__init__(uid)

    def get_position(self) -> Tuple[float, float]:
        if not self.transform:
            return (0.0, 0.0)
        return self.transform.position.x, self.transform.position.y

