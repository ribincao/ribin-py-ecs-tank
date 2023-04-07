from logic.interface.component import Component
from logic.component.create_component import CreateComponent
from logic.component.transform_component import TransformComponent
from logic.component.move_component import MoveComponent
from logic.component.rigibody_component import RigibodyComponent
from logic.component.box_collider_component import BoxColliderComponent
from logic.component.state_component import StateComponent
from logic.component.model_component import ModelComponent
from logic.component.player_component import PlayerComponent
from typing import Optional, Tuple
from logic.manager.component_manager import component_manager


class GameLogicEntity(object):

    def __init__(self, uid: int, is_async: bool = True):
        self.uid: int = uid
        self.is_async: bool = is_async

        self.transform: TransformComponent = TransformComponent()
        self.create: Optional[CreateComponent] = None
        self.move: Optional[MoveComponent] = None
        self.rigibody: Optional[RigibodyComponent] = None
        self.box_collider: Optional[BoxColliderComponent] = None
        self.state: Optional[StateComponent] = None
        self.model: Optional[ModelComponent] = None
        self.player: Optional[PlayerComponent] = None

    def export(self) -> dict:
        if not self.is_async:
            return {}
        if not self.create or not self.create.create_status:
            return {}
        d = {}
        for k, v in self.__dict__.items():
            if not v or not isinstance(v, Component):
                continue
            component = v.serialize()
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

    def add_create(self, create_status: bool, node_data: dict):
        if not self.create:
            self.create = CreateComponent()
        self.create.create_status = create_status
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

