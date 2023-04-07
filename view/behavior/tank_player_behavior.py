from view.interface.pygame_behavior import PyGameBehavior
from logic.entity.entity import GameLogicEntity
from typing import Tuple


class TankPlayerBehavior(PyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankPlayerBehavior, self).__init__(entity)

    async def update(self):
        pass

    def init_models(self):
        self._load_models("tank", "player")
