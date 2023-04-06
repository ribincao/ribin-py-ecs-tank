from view.behavior.behavior import PyGameBehavior
from common.singleton import Singleton
from logic.entity.entity import GameLogicEntity


class BehaviorManager(Singleton):

    def __init__(self):
        pass

    def get_tank_behavior(self, entity: GameLogicEntity) -> PyGameBehavior:
        return PyGameBehavior(entity)

behavior_manager = BehaviorManager()

