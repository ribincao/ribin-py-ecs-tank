from logic.component.create_component import CreateComponent
from logic.component.transform_component import TransformComponent
from logic.component.move_component import MoveComponent
from logic.component.rigibody_component import RigibodyComponent
from logic.component.box_collider_component import BoxColliderComponent
from logic.component.state_component import StateComponent
from logic.component.model_component import ModelComponent
from typing import Optional
from logic.entity.state import EntityState
from logic.component.transform_component import Vector2


class GameLogicEntity(object):

    def __init__(self, uid: int):
        self.uid: int = uid

        self.transform: Optional[TransformComponent] = None
        self.create: Optional[CreateComponent] = None
        self.move: Optional[MoveComponent] = None
        self.rigibody: Optional[RigibodyComponent] = None
        self.box2d_collider: Optional[BoxColliderComponent] = None
        self.state: Optional[StateComponent] = None
        self.model: Optional[ModelComponent] = None

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

    def add_transform(self, new_position: Vector2):
        if not self.transform:
            self.transform = TransformComponent()
        self.transform.position = new_position
        self.transform.last_position = new_position

    def add_move(self, new_speed: float):
        if not self.move:
            self.move = MoveComponent()
        self.move.speed = new_speed

    def add_create(self, new_mod_name: str):
        if not self.create:
            self.create = CreateComponent()
        self.create.mod_name = new_mod_name
    
    def add_box_collider(self, width: float, height: float):
        if not self.box2d_collider:
            self.box2d_collider = BoxColliderComponent()
        self.box2d_collider.height = height
        self.box2d_collider.width = width

