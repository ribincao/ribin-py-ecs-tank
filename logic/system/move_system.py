from common.logger import logger
from logic.system.system import System
from logic.context import Context
from logic.entity.state import EntityState
from logic.command.move_command import UP, DOWN, LEFT, RIGHT
from logic.event.event import EntityCreateEvent


class MoveSystem(System):

    def __init__(self, context: Context):
        super(MoveSystem, self).__init__(context)
        self.context.register_event("EntityCreateEvent", self.on_entity_create)

    async def update(self):
        logger.debug("MoveSystem Update")
        entities = self.context.get_entities()
        for entity in entities:
            if not entity.transform or not entity.move or entity.move.speed <= 0:
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

    def on_entity_create(self, event: EntityCreateEvent):
        logger.debug(f"MoveListenEvent {event.uid} created.")
