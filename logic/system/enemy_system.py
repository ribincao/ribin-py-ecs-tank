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
        entities = self.context.get_entities()
        for entity in entities:
            if not entity.model:
                continue
            if entity.model.model_name != "enemy":
                continue
            if entity.transform.last_position != entity.transform.position:
                continue
            entity.transform.rotation = (entity.transform.rotation + 90) % 360
        pass

