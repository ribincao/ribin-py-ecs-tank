from logic.interface.system import System
from logic.context import Context
from common.logger import logger
from logic.entity.entity import GameLogicEntity
from logic.component.state_component import State


class ColliderSystem(System):

    def __init__(self, context: Context):
        super(ColliderSystem, self).__init__(context)

    async def update(self):
        entities = self.context.get_entities()
        for entityA in entities:
            if not entityA.box_collider:
                continue
            # 先做个简单的,只判断玩家和子弹,后面抽象优化
            if not entityA.model or entityA.model.model_name not in ["player1", "player2", "bullet"]:
                continue

            for entityB in entities:
                if not entityB.box_collider:
                    continue
                if entityA.box_collider.layer != entityB.box_collider.layer:
                    continue
                if entityA.uid == entityB.uid:
                    continue

                positionA = entityA.transform.position
                heightA = entityA.box_collider.height
                widthA = entityA.box_collider.width

                positionB = entityB.transform.position
                heightB = entityB.box_collider.height
                widthB = entityB.box_collider.width

                collider_direction, collider = 0, False
                if positionA[0] >= positionB[0] and positionA[1] >= positionB[1]:
                    distanceX = positionA[0] - positionB[0]
                    distanceY = positionA[1] - positionB[1]
                    if distanceX < widthB and distanceY < heightA:
                        collider = True
                        entityA.box_collider.collider_direction = (-1, -1)
                        collider_direction = 1
                elif positionA[0] >= positionB[0] and positionA[1] < positionB[1]:
                    distanceX = positionA[0] - positionB[0]
                    distanceY = positionB[1] - positionA[1]
                    if distanceX < widthA and distanceY < heightA:
                        collider = True
                        entityA.box_collider.collider_direction = (1, -1)
                        collider_direction = 2
                        logger.debug(f"2. box collider detect {entityA.uid} -> {entityB.uid}")
                elif positionA[0] < positionB[0] and positionA[1] < positionB[1]:
                    distanceX = positionB[0] - positionA[0]
                    distanceY = positionB[1] - positionA[1]
                    if distanceX < widthA and distanceY < heightB:
                        collider = True
                        entityA.box_collider.collider_direction = (1, 1)
                        collider_direction = 3
                        logger.debug(f"3. box collider detect {entityA.uid} -> {entityB.uid}")
                elif positionA[0] < positionB[0] and positionA[1] >= positionB[1]:
                    distanceX = positionB[0] - positionA[0]
                    distanceY = positionA[1] - positionB[1]
                    if distanceX < widthB and distanceY < heightB:
                        collider = True
                        entityA.box_collider.collider_direction = (-1, 1)
                        collider_direction = 4

                if collider:
                    logger.info(f"box collider detect {collider_direction}: {entityA.uid} -> {entityB.uid}")
