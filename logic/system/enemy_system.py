from logic.matrix.system import System
from logic.matrix.context import Context
from logic.logic_entity import GameLogicEntity
from typing import List, Optional, Tuple
import random


class EnemySystem(System):
    MAX_CNT = 3

    def __init__(self, context: Context):
        super(EnemySystem, self).__init__(context)
        self.slot: List[Optional[GameLogicEntity]] = [None for _ in range(self.MAX_CNT)]
        self.positions: List[Tuple[float, float]] = [(0, 0), (360, 0), (720, 0)]

    def get_random_rotate(self):
        return random.choice([0, 90, 180, 270])

    def update(self):
        entities = list(self.context.entities)
        for entity in entities:
            if not entity.model or not entity.transform:
                continue
            if entity.model.model_name != "enemy":
                continue
            if entity.transform.last_position != entity.transform.position:
                continue
            entity.transform.rotation = self.get_random_rotate()

