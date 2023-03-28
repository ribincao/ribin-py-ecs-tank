from common.logger import logger
from logic.system.isystem import ISystem
from logic.context import Context
from logic.entity.state import EntityState
from logic.command.move_command import UP, DOWN, LEFT, RIGHT


class MoveSystem(ISystem):

    def __init__(self, context: Context):
        super(MoveSystem, self).__init__(context)

    async def update(self):
        logger.debug("MoveSystem Update")
        entities = self.context.get_entities()
        for entity in entities:
            if not entity.transform or not entity.move:
                continue
            if entity.state == EntityState.move:
                if entity.mod_index == UP:
                    entity.transform.position.y -= entity.move.speed
                if entity.mod_index == DOWN:
                    entity.transform.position.y += entity.move.speed
                if entity.mod_index == LEFT:
                    entity.transform.position.x -= entity.move.speed
                if entity.mod_index == RIGHT:
                    entity.transform.position.x += entity.move.speed
            if entity.rigibody:
                entity.transform.position.y += entity.rigibody.gravity
