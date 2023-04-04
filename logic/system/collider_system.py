from logic.system.system import System
from logic.context import Context
from common.logger import logger
from logic.entity.entity import GameLogicEntity


class ColliderSystem(System):

    def __init__(self, context: Context):
        super(ColliderSystem, self).__init__(context)

    async def update(self):
        entities = self.context.get_entities()
        for entityA in entities:
            if not entityA.box2d_collider:
                continue
            # 先做个简单的,只判断玩家和子弹,后面抽象优化
            if entityA.create.mod_name not in ["player1", "player2", "bullet"]:
                continue

            for entityB in entities:
                if not entityB.box2d_collider or entityA.uid == entityB.uid:
                    continue

                positionA = entityA.transform.position.to_tuple()
                heightA = entityA.box2d_collider.height
                widthA = entityA.box2d_collider.width

                positionB = entityB.transform.position.to_tuple()
                heightB = entityB.box2d_collider.height
                widthB = entityB.box2d_collider.width

                collider = False
                if positionA[0] >= positionB[0] and positionA[1] >= positionB[1]:
                    distanceX = positionA[0] - positionB[0]
                    distanceY = positionA[1] - positionB[1]
                    if distanceX <= widthB and distanceY <= heightA:
                        collider = True
                        logger.info(f"1. box collider detect {entityA.create.mod_name} -> {entityB.create.mod_name}")
                elif positionA[0] >= positionB[0] and positionA[1] < positionB[1]:
                    distanceX = positionA[0] - positionB[0]
                    distanceY = positionB[1] - positionA[1]
                    if distanceX <= widthA and distanceY <= heightA:
                        collider = True
                        logger.info(f"1. box collider detect {entityA.create.mod_name} -> {entityB.create.mod_name}")
                elif positionA[0] < positionB[0] and positionA[1] < positionB[1]:
                    distanceX = positionB[0] - positionA[0]
                    distanceY = positionB[1] - positionA[1]
                    if distanceX <= widthA and distanceY <= heightB:
                        collider = True
                        logger.info(f"1. box collider detect {entityA.create.mod_name} -> {entityB.create.mod_name}")
                elif positionA[0] < positionB[0] and positionA[1] >= positionB[1]:
                    distanceX = positionB[0] - positionA[0]
                    distanceY = positionA[1] - positionB[1]
                    if distanceX <= widthB and distanceY <= heightB:
                        collider = True
                        logger.info(f"1. box collider detect {entityA.create.mod_name} -> {entityB.create.mod_name}")

                if collider:
                    logger.debug(f"box collider detect {entityA.create.mod_name} -> {entityB.create.mod_name}")
