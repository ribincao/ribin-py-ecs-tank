from view.interface.behavior import PyGameBehavior
from common.singleton import Singleton
from logic.entity.entity import GameLogicEntity
from view.behavior.tank_player_behavior import TankPlayerBehavior
from view.behavior.tank_wall_behavior import TankWallBehavior
from view.behavior.tank_symbol_behavior import TankSymbolBehavior
from view.behavior.tank_iron_behavior import TankIronBehavior
from view.behavior.tank_water_behavior import TankWaterBehavior
from view.behavior.tank_grass_behavior import TankGrassBehavior
from view.behavior.tank_enemy_behavior import TankEnemyBehavior
from view.behavior.tank_bullet_behavior import TankBulletBehavior


class BehaviorManager(Singleton):

    def __init__(self):
        pass

    def get_tank_behavior(self, entity: GameLogicEntity) -> PyGameBehavior:
        if not entity.model or not entity.model.model_name:
            return TankPlayerBehavior(entity)

        if entity.model.model_name == "wall":
            return TankWallBehavior(entity)
        if entity.model.model_name == "iron":
            return TankIronBehavior(entity)
        if entity.model.model_name == "bullet":
            return TankBulletBehavior(entity)
        if entity.model.model_name == "enemy":
            return TankEnemyBehavior(entity)
        if entity.model.model_name == "symbol":
            return TankSymbolBehavior(entity)
        if entity.model.model_name == "water":
            return TankWaterBehavior(entity)
        if entity.model.model_name == "grass":
            return TankGrassBehavior(entity)

        return TankPlayerBehavior(entity)


behavior_manager = BehaviorManager()
