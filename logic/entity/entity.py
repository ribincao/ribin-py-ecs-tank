from logic.interface.component import Component
from logic.component.create_component import CreateComponent
from logic.component.transform_component import TransformComponent
from logic.component.move_component import MoveComponent
from logic.component.rigibody_component import RigibodyComponent
from logic.component.box_collider_component import BoxColliderComponent
from logic.component.state_component import StateComponent
from logic.component.model_component import ModelComponent
from logic.component.player_component import PlayerComponent
from logic.component.bullet_component import BulletComponent
from typing import Optional, Tuple
from logic.manager.component_manager import component_manager


class GameLogicEntity(object):

    def __init__(self, uid: int, is_async: bool = True):
        self.uid: int = uid
        self.is_async: bool = is_async
        self._components = {}

        self.create: CreateComponent = CreateComponent()
        self.transform: TransformComponent = TransformComponent()
        self.state: StateComponent = StateComponent()
        self.move: Optional[MoveComponent] = None
        self.rigibody: Optional[RigibodyComponent] = None
        self.box_collider: Optional[BoxColliderComponent] = None
        self.model: Optional[ModelComponent] = None
        self.player: Optional[PlayerComponent] = None
        self.bullet: Optional[BulletComponent] = None

    def has(self, *t_comps):
        if len(t_comps) == 1:
            return t_comps[0] in self._components
        return all([t_comp in self._components for t_comp in t_comps])

    def has_any(self, *t_comps):
        if len(t_comps) == 1:
            return t_comps[0] in self._components
        return any([t_comp in self._components for t_comp in t_comps])

    def export(self) -> dict:
        if not self.is_async:
            return {}
        if not self.create.is_created:
            return {}
        d = {}
        for k, v in self.__dict__.items():
            if not v or not isinstance(v, Component):
                continue
            component = v.serialize()
            if not component:
                continue
            d[k] = component
        return d

    def update(self, snap: dict):
        for name, new_component in snap.items():
            component = self.__dict__.get(name, None)
            if not component:
                component = component_manager.get_component(name)
            component.__dict__.update(new_component)
            self.__dict__[name] = component

    def add_transform(self, position: Tuple[float, float], rotation: float = 0.0):
        if not self.transform:
            self.transform = TransformComponent()
        self.transform.position = position
        self.transform.rotation = rotation
        self.transform.last_position = position

    def add_move(self, speed: float):
        if not self.move:
            self.move = MoveComponent()
        self.move.speed = speed

    def add_create(self, is_created: bool, node_data: dict):
        if not self.create:
            self.create = CreateComponent()
        self.create.is_created = is_created
        self.create.node_data = node_data
    
    def add_box_collider(self, width: float, height: float, collider_direction: Tuple[int, int], layer: int):
        if not self.box_collider:
            self.box_collider = BoxColliderComponent()
        self.box_collider.height = height
        self.box_collider.width = width
        self.box_collider.collider_direction = collider_direction
        self.box_collider.layer = layer

    def add_state(self, state: int):
        if not self.state:
            self.state = StateComponent()
        self.state.state = state

    def add_model(self, model_index: int, model_name: str):
        if not self.model:
            self.model = ModelComponent()
        self.model.model_index = model_index
        self.model.model_name = model_name

    def add_player(self, player_id: str):
        if not self.player:
            self.player = PlayerComponent()
        self.player.player_id = player_id

