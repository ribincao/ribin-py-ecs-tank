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
            x, y = entity.transform.position.to_tuple()
            if entity.state == EntityState.move:
                if entity.mod_index == UP:
                    y -= entity.move.speed
                if entity.mod_index == DOWN:
                    y += entity.move.speed
                if entity.mod_index == LEFT:
                    x -= entity.move.speed
                if entity.mod_index == RIGHT:
                    x += entity.move.speed


            entity.transform.position.x = x
            entity.transform.position.y = y
            if entity.create.mod_name != "bullet":
                entity.transform.position.x = min(max(x, 0), self.context.edge_size[0] - 60)
                entity.transform.position.y = min(max(0, y), self.context.edge_size[1] - 60)

    def on_entity_create(self, event: EntityCreateEvent):
        logger.debug(f"MoveListenEvent {event.uid} created.")

