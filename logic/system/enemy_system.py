from logic.interface.system import System
from logic.context import Context
from logic.entity.entity import GameLogicEntity
from typing import List, Optional, Tuple


class EnemySystem(System):
    MAX_CNT = 3

    def __init__(self, context: Context):
        super(EnemySystem, self).__init__(context)
        self.slot: List[Optional[GameLogicEntity]] = [None for _ in range(self.MAX_CNT)]
        self.positions: List[Tuple[float, float]] = [(0, 0), (360, 0), (720, 0)]

    async def update(self):
        for idx in range(len(self.slot)):
            if self.slot[idx]:
                continue
            entity = self.context.create_entity()
            entity.add_create("enemy2")
            entity.add_transform(self.positions[idx])
            entity.add_move(3)
            self.slot[idx] = entity

