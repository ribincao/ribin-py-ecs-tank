from interface.context import IContext
from abc import abstractmethod
from typing import List, Dict
from interface.behavior import IBehavior
from pygame import Surface, Color


class IView(object):
    VIEW_RATE = 100e-3

    def __init__(self, context: IContext):
        self.context: IContext = context
        self.scenes: Dict[str, Surface] = {}
        self.scene_id: str = ""  # 场景id, 不同关卡
        self.back_ground: Color = Color(0, 0, 0)

    @abstractmethod
    def init_view(self):
        # 初始化所有的关卡scene
        pass

    def get_behaviors(self) -> List[IBehavior]:
        return self.context.get_behaviors()

    def get_scene(self) -> Surface:
        return self.scenes[self.scene_id]

    @abstractmethod
    async def handle_event(self, operation: int):
        pass

