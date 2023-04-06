from view.behavior.behavior import PyGameBehavior
from logic.entity.entity import GameLogicEntity
from logic.component.move_component import MoveDirection
from typing import Tuple


class TankBehavior(PyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankBehavior, self).__init__(entity)

    def get_bullet_position(self) -> Tuple[float, float]:
        position = self.entity.transform.position
        if not self.entity.model or not self.rect:
            return 0, 0

        if self.entity.model.model_index == MoveDirection.UP:
            return position[0] + self.rect.width / 2 - 6, position[1]
        elif self.entity.model.model_index == MoveDirection.DOWN:
            return position[0] + self.rect.width / 2 - 6, position[1] + self.rect.height
        elif self.entity.model.model_index == MoveDirection.LEFT:
            return position[0], position[1] + self.rect.height / 2 - 6
        elif self.entity.model.model_index == MoveDirection.RIGHT:
            return position[0] + self.rect.width, position[1] + self.rect.height / 2 - 6  #  bullet_size: 12 x 12

        return 0.0, 0.0

    async def update(self):
        pass

