from common.logger import logger
from logic.matrix.system import System
from logic.matrix.context import Context
from logic.manager.component_manager import component_manager
from logic.matrix.group import Group
from logic.matrix.matcher import Matcher


class CreateSystem(System):

    def __init__(self, context: Context):
        super(CreateSystem, self).__init__(context)
        self.create_group: Group = self.context.get_group(Matcher("create"))
        self.entity_count: int = 0

    def update(self):
        for entity in self.create_group.entities:
            if entity.get_component("create").is_created:
                continue
            node_data = entity.get_component("create").node_data
            for name, value in node_data.items():
                component = component_manager.get_component(name)
                if not component:
                    continue
                component.__dict__.update(value)
                entity.add_component(component)
            entity.get_component("create").is_created = True
            self.entity_count += 1
            logger.debug(f"CreateSystem {self.entity_count}| {entity.uid} - {node_data}")
            

