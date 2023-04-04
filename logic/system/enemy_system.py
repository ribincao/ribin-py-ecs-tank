from common.logger import logger
from logic.system.system import System
from logic.context import Context
from logic.entity.entity import GameLogicEntity
from typing import List, Optional
from common.common import Vector2


class EnemySystem(System):
    MAX_CNT = 3

    def __init__(self, context: Context):
        super(EnemySystem, self).__init__(context)
        self.slot: List[Optional[GameLogicEntity]] = [None for _ in range(self.MAX_CNT)]
        self.positions: List[Vector2] = [Vector2(0, 0), Vector2(360, 0), Vector2(720, 0)]

    async def update(self):
        for idx in range(len(self.slot)):
            if self.slot[idx]:
                continue
            entity = self.context.create_entity()
            entity.add_create("enemy2")
            entity.add_transform(self.positions[idx])
            entity.add_move(3)
            self.slot[idx] = entity

