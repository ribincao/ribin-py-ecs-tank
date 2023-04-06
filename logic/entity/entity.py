from logic.component.create_component import CreateComponent
from logic.component.transform_component import TransformComponent
from logic.component.move_component import MoveComponent
from logic.component.rigibody_component import RigibodyComponent
from logic.component.box_collider_component import BoxColliderComponent
from logic.component.state_component import StateComponent
from logic.component.model_component import ModelComponent
from logic.component.player_component import PlayerComponent
from typing import Optional, Tuple


class GameLogicEntity(object):

    def __init__(self, uid: int):
        self.uid: int = uid

        self.transform: Optional[TransformComponent] = None
        self.create: Optional[CreateComponent] = None
        self.move: Optional[MoveComponent] = None
        self.rigibody: Optional[RigibodyComponent] = None
        self.box_collider: Optional[BoxColliderComponent] = None
        self.state: Optional[StateComponent] = None
        self.model: Optional[ModelComponent] = None
        self.player: Optional[PlayerComponent] = None

    def export(self) -> dict:
        if not self.create:
            return {}
        d = dict()
        d["uid"] = self.uid
        d["mod_index"] = self.mod_index
        d["transform"] = {}
        d["transform"]["position"] = self.transform.position.to_tuple()
        d["create"] = {}
        d["create"]["mod_name"] = self.create.mod_name
        d["create"]["mod_type"] = self.create.mod_type
        d["move"] = {}
        d["move"]["speed"] = self.move.speed
        return d

    def refresh(self, info: dict):
        self.transform.position.x = info["transform"]["position"][0]
        self.transform.position.y = info["transform"]["position"][1]
        self.create.mod_name = info["create"]["mod_name"]
        self.create.mod_type = info["create"]["mod_type"]
        self.move.speed = info["move"]["speed"]
        self.mod_index = info.get("mod_index", 0)

    def add_transform(self, position: Tuple[float, float]):
        if not self.transform:
            self.transform = TransformComponent()
        self.transform.position = position
        self.transform.last_position = position

    def add_move(self, speed: float, direction: int):
        if not self.move:
            self.move = MoveComponent()
        self.move.speed = speed
        self.move.direction = direction

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

