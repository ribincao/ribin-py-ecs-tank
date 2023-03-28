from typing import Tuple
from logic.component.create_component import CreateComponent
from logic.component.transform_component import TransformComponent
from logic.component.move_component import MoveComponent
from logic.component.rigibody_component import RigibodyComponent
from typing import Optional
from logic.entity.state import EntityState


class GameLogicEntity(object):

    def __init__(self, uid: int):
        self.uid: int = uid
        self.mod_id: int = -1
        self.state: int = EntityState.normal  # 维护状态
        self.mod_index: int = 0

        self.transform: Optional[TransformComponent] = None
        self.create: Optional[CreateComponent] = None
        self.move: Optional[MoveComponent] = None
        self.rigibody: Optional[RigibodyComponent] = None

    def get_position(self) -> Tuple[float, float]:
        if not self.transform:
            return 0.0, 0.0
        return self.transform.position.x, self.transform.position.y
