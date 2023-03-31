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
        self.create: Optional[CreateComponent] = None
        self.move: Optional[MoveComponent] = None
        self.rigibody: Optional[RigibodyComponent] = None

    def export(self) -> dict:
        if not self.create or not self.create.mod_name.startswith("player"):
            return {}
        d = dict()
        d["uid"] = self.uid
        d["mod_index"] = self.mod_index
        d["transform"] = {}
        d["transform"]["position"] = self.transform.position.to_tuple()
        return d

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
