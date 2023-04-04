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
                    if entity.box2d_collider and entity.box2d_collider.collider_direction[1] == -1:
                        continue
                    y -= entity.move.speed
                if entity.mod_index == DOWN:
                    if entity.box2d_collider and entity.box2d_collider.collider_direction[1] == 1:
                        continue
                    y += entity.move.speed
                if entity.mod_index == LEFT:
                    if entity.box2d_collider and entity.box2d_collider.collider_direction[0] == -1:
                        continue
                    x -= entity.move.speed
                if entity.mod_index == RIGHT:
                    if entity.box2d_collider and entity.box2d_collider.collider_direction[0] == 1:
                        continue
                    x += entity.move.speed

            if entity.rigibody:
                y += entity.rigibody.gravity

            if entity.box2d_collider and  self.check_edge(x, y, entity.box2d_collider.width, entity.box2d_collider.height):
                continue

            entity.transform.position.x = x
            entity.transform.position.y = y

    def on_entity_create(self, event: EntityCreateEvent):
        logger.debug(f"MoveListenEvent {event.uid} created.")

    def check_edge(self, x: float, y: float, width: float, height: float) -> bool:
        if x < 0 or y < 0:
            return True

        if x + width > self.context.edge_size[0] or y + height > self.context.edge_size[1]:
            return True

        return False

