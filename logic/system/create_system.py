from common.logger import logger
from logic.matrix.system import System
from logic.matrix.context import Context
from logic.manager.component_manager import component_manager


class CreateSystem(System):

    def __init__(self, context: Context):
        super(CreateSystem, self).__init__(context)
        self.entity_count: int = 0

    def update(self):
        entities = list(self.context.entities)
        for entity in entities:
            if entity.create.is_created:
                continue
            node_data = entity.create.node_data
            for name, value in node_data.items():
                component = component_manager.get_component(name)
                if not component:
                    continue
                component.__dict__.update(value)
                entity.__dict__[name] = component
            entity.create.is_created = True
            self.entity_count += 1
            logger.debug(f"CreateSystem {self.entity_count}| {entity.uid} - {node_data}")
            

