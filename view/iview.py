from logic.context import Context
from abc import abstractmethod
from typing import List, Dict
from view.behavior.ibehavior import IPyGameBehavior


class IView(object):
    VIEW_RATE = 100e-3

    def __init__(self, context: Context):
        self.behaviors: Dict[int, IPyGameBehavior] = {}
        self.context: Context = context
        self.scenes: Dict[int, object] = {}
        self.scene_id: int = 0  # 场景id, 不同关卡
        self.back_ground = (0, 0, 0)

    @abstractmethod
    async def update(self):
        pass

    @abstractmethod
    def init_view(self):
        # 初始化所有的关卡scene
        pass

    def get_behaviors(self) -> List[IPyGameBehavior]:
        return list(self.behaviors.values())

    @abstractmethod
    async def handle_event(self, operation: str):
        pass
