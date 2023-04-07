from common.logger import logger
from logic.interface.system import System
from logic.context import Context
from logic.manager.component_manager import component_manager


class CreateSystem(System):

    def __init__(self, context: Context):
        super(CreateSystem, self).__init__(context)
        self.entity_count: int = 0

    async def update(self):
        entities = self.context.get_entities()
        for entity in entities:
            if not entity.create or entity.create.create_status:
                continue
            node_data = entity.create.node_data
            for name, value in node_data.items():
                component = component_manager.get_component(name)
                if not component:
                    continue
                component.__dict__.update(value)
                entity.__dict__[name] = component
            entity.create.create_status = True
            self.entity_count += 1
            logger.debug(f"CreateSystem {self.entity_count}| {entity.uid} - {node_data}")
            

