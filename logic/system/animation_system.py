from common.logger import logger
from logic.interface.system import System
from logic.context import Context
from logic.event.event import EntityCreateEvent, EntityDestroyEvent


class AnimationSystem(System):

    def __init__(self, context: Context):
        super(AnimationSystem, self).__init__(context)
        self.context.register_event("EntityCreateEvent", self.on_entity_create)
        self.context.register_event("EntityDestroyEvent", self.on_entity_create)

    def update(self):
        entities = self.context.get_entities()

    def on_entity_create(self, event: EntityCreateEvent):
        logger.info(f"AnimationSystemListen {event.uid} created.")

    def on_entity_destroy(self, event: EntityDestroyEvent):
        logger.info(f"AnimationSystemListen {event.uid} destroyed.")
