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


component_manager = ComponentManager()


