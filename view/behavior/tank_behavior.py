from view.behavior.behavior import PyGameBehavior
from logic.entity.entity import GameLogicEntity
from typing import Tuple


class TankBehavior(PyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankBehavior, self).__init__(entity)

    def get_bullet_position(self) -> Tuple[float, float]:
        position = self.entity.transform.position
        if not self.entity.model or not self.rect:
            return 0, 0

        if self.entity.transform.rotation == 0:
            return position[0], position[1] - self.rect.height / 2
        elif self.entity.transform.rotation == 180:
            return position[0], position[1] + self.rect.height / 2
        elif self.entity.transform.rotation == 90:
            return position[0] - self.rect.width / 2, position[1]
        elif self.entity.transform.rotation == 270:
            return position[0] + self.rect.width / 2, position[1]

        return 0.0, 0.0

    async def update(self):
        pass

