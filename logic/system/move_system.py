from common.logger import logger
from logic.interface.system import System
from logic.context import Context
from logic.component.state_component import State
from logic.component.move_component import MoveDirection
from logic.event.event import EntityCreateEvent


class MoveSystem(System):

    def __init__(self, context: Context):
        super(MoveSystem, self).__init__(context)
        self.context.register_event("EntityCreateEvent", self.on_entity_create)

    async def update(self):
        entities = self.context.get_entities()
        for entity in entities:
            if not entity.transform or not entity.move or entity.move.speed <= 0:
                continue
            if not entity.state:
                continue
            x, y = entity.transform.position

            entity.transform.last_position = (x, y)
            if entity.state.state == State.move:
                if entity.move.direction == MoveDirection.UP:
                    y -= entity.move.speed
                if entity.move.direction == MoveDirection.DOWN:
                    y += entity.move.speed
                if entity.move.direction == MoveDirection.LEFT:
                    x -= entity.move.speed
                if entity.move.direction == MoveDirection.RIGHT:
                    x += entity.move.speed

            if entity.box_collider:
                x = min(max(x, entity.box_collider.width / 2), self.context.edge_size[0] - entity.box_collider.width / 2)
                y = min(max(y, entity.box_collider.height / 2), self.context.edge_size[1] - entity.box_collider.height / 2)
            entity.transform.position = (x, y)

    def on_entity_create(self, event: EntityCreateEvent):
        logger.debug(f"MoveListenEvent {event.uid} created.")

