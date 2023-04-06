from view.behavior.behavior import PyGameBehavior
from common.singleton import Singleton
from logic.entity.entity import GameLogicEntity
from view.behavior.tank_behavior import TankBehavior
from view.behavior.tank_wall_behavior import TankWallBehavior
from view.behavior.tank_symbol_behavior import TankSymbolBehavior
from view.behavior.tank_steel_behavior import TankSteelBehavior
from view.behavior.tank_enemy_behavior import TankEnemyBehavior
from view.behavior.tank_bullet_behavior import TankBulletBehavior


class BehaviorManager(Singleton):

    def __init__(self):
        pass

    def get_tank_behavior(self, entity: GameLogicEntity) -> PyGameBehavior:
        if not entity.model or not entity.model.model_name:
            return TankBehavior(entity)

        if entity.model.model_name == "wall":
            return TankWallBehavior(entity)
        if entity.model.model_name == "steel":
            return TankSteelBehavior(entity)
        if entity.model.model_name == "bullet":
            return TankBulletBehavior(entity)
        if entity.model.model_name == "enemy":
            return TankEnemyBehavior(entity)
        if entity.model.model_name == "symbol":
            return TankSymbolBehavior(entity)

        return TankBehavior(entity)


behavior_manager = BehaviorManager()
