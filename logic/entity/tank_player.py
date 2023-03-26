from interface.entity import IEntity
from logic.component.transform_component import TransformComponent
from typing import Tuple


class TankPlayer(IEntity):

    def __init__(self, uid: int):
        super(TankPlayer, self).__init__(uid)
        self.transform: TransformComponent = TransformComponent()

    def get_position(self) -> Tuple[float, float]:
        return self.transform.position.x, self.transform.position.y

