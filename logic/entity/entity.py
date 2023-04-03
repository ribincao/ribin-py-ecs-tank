from typing import Tuple
from logic.component.create_component import CreateComponent
from logic.component.transform_component import TransformComponent
from logic.component.move_component import MoveComponent
from logic.component.rigibody_component import RigibodyComponent
from typing import Optional
from logic.entity.state import EntityState
from common.common import Vector2


class GameLogicEntity(object):

    def __init__(self, uid: int):
        self.uid: int = uid
        self.state: int = EntityState.normal  # 维护状态
        self.mod_index: int = 0
        self.layer: int = 0

        self.transform: TransformComponent = TransformComponent()
        self.create: CreateComponent = CreateComponent()
        self.move: MoveComponent = MoveComponent()
        self.rigibody: Optional[RigibodyComponent] = None

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

    def add_move(self, new_speed: float):
        if not self.move:
            self.move = MoveComponent()
        self.move.speed = new_speed

    def add_create(self, new_mod_name: str):
        if not self.create:
            self.create = CreateComponent()
        self.create.mod_name = new_mod_name
