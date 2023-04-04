from view.behavior.behavior import PyGameBehavior
from logic.entity.entity import GameLogicEntity
from logic.system.move_system import UP, DOWN, LEFT, RIGHT
from typing import Tuple


class TankBehavior(PyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankBehavior, self).__init__(entity)

    def get_bullet_position(self) -> Tuple[float, float]:
        position = self.entity.transform.position
        if self.entity.mod_index == UP:
            return position.x + self.rect.width / 2 - 6, position.y
        elif self.entity.mod_index == DOWN:
            return position.x + self.rect.width / 2 - 6, position.y + self.rect.height
        elif self.entity.mod_index == LEFT:
            return position.x, position.y + self.rect.height / 2 - 6
        elif self.entity.mod_index == RIGHT:
            return position.x + self.rect.width, position.y + self.rect.height / 2 - 6  #  bullet_size: 12 x 12

        return 0.0, 0.0

