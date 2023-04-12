from common.singleton import Singleton
from logic.matrix.component import Component
from logic.component.transform_component import TransformComponent
from logic.component.move_component import MoveComponent
from logic.component.create_component import CreateComponent
from logic.component.box_collider_component import BoxColliderComponent
from logic.component.rigibody_component import RigibodyComponent
from logic.component.state_component import StateComponent
from logic.component.model_component import ModelComponent
from logic.component.player_component import PlayerComponent
from logic.component.bullet_component import BulletComponent
from typing import Optional, Dict
from copy import deepcopy


class ComponentManager(Singleton):

    def __init__(self):
        self._component_map: Dict[str, Component] = {}
        self._init_component_manager()

    def get_component(self, component_name: str) -> Optional[Component]:
        instance = self._component_map.get(component_name, None)
        return deepcopy(instance)

    def _register_component(self, component: Component):
        self._component_map[component.name] = component

    def _init_component_manager(self):
        self._register_component(TransformComponent())
        self._register_component(MoveComponent())
        self._register_component(CreateComponent())
        self._register_component(BoxColliderComponent())
        self._register_component(RigibodyComponent())
        self._register_component(StateComponent())
        self._register_component(ModelComponent())
        self._register_component(PlayerComponent())
        self._register_component(BulletComponent())

    def generate_logic_entity(self):
        i_entity = '''from logic.matrix.entity import Entity\n'''
        i_component = '''from logic.manager.component_manager import *\n\n'''
        e_init = '''\nclass GameLogicEntity(Entity):\n\n\tdef __init__(self):\n\t\tsuper(GameLogicEntity, self).__init__()\n\n'''
        t_component = '''\t@property\n\tdef {component_name}(self) -> Optional[{component_class_name}]:\n\t\treturn self._get_component("{component_name}")\n\n'''

        code = i_entity + i_component + e_init
        for component_name, component_inst in self._component_map.items():
            component_code = t_component.format(component_name=component_name,
                                                component_class_name=component_inst.__class__.__name__)
            code += component_code
        self._output_file(code)

    @staticmethod
    def _output_file(file_data: str, file_name: str = "../logic_entity.py"):
        with open(file_name, "w") as file:
            file.write(file_data)


component_manager = ComponentManager()


if __name__ == '__main__':
    component_manager.generate_logic_entity()


