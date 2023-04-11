from logic.matrix.system import System
from logic.matrix.context import Context
from logic.matrix.entity import GameLogicEntity
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
            if not entity.get_component("model"):
                continue
            if entity.get_component("model").model_name != "enemy":
                continue
            if entity.get_component("transform").last_position != entity.get_component("transform").position:
                continue
            entity.get_component("transform").rotation = self.get_random_rotate()

