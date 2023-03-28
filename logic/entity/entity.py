from typing import Tuple
from logic.component.create_component import CreateComponent
from logic.component.transform_component import TransformComponent
from typing import Optional


class GameLogicEntity(object):

    def __init__(self, uid: int):
        self.uid: int = uid
        self.mod_id: int = -1
        self.state: str = ''  # 维护状态
        
        self.transform: Optional[TransformComponent] = None
        self.create: Optional[CreateComponent] = None

    def get_position(self) -> Tuple[float, float]:
        if not self.transform:
            return (0.0, 0.0)
        return self.transform.position.x, self.transform.position.y
