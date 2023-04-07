from view.interface.pygame_behavior import PyGameBehavior
from logic.entity.entity import GameLogicEntity
from typing import Tuple


class TankPlayerBehavior(PyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankPlayerBehavior, self).__init__(entity)

    def get_forward(self) -> Tuple[Tuple[float, float], float]:
        position = self.entity.transform.position
        if not self.entity.model or not self.rect:
            return (0.0, 0.0), 0.0

        if self.entity.transform.rotation == 0:
            return (position[0], position[1] - self.rect.height / 2), self.entity.transform.rotation
        elif self.entity.transform.rotation == 180:
            return (position[0], position[1] + self.rect.height / 2), self.entity.transform.rotation
        elif self.entity.transform.rotation == 90:
            return (position[0] - self.rect.width / 2, position[1]), self.entity.transform.rotation
        elif self.entity.transform.rotation == 270:
            return (position[0] + self.rect.width / 2, position[1]), self.entity.transform.rotation

        return (0.0, 0.0), 0.0

    async def update(self):
        pass

    def init_models(self):
        self._load_models("tank", "player")
