from logic.context import Context
from abc import abstractmethod
from typing import List, Dict, Tuple
from view.interface.pygame_behavior import PyGameBehavior


class View(object):
    VIEW_RATE = 20e-3

    def __init__(self, context: Context):
        self.behaviors: Dict[int, PyGameBehavior] = {}
        self.context: Context = context
        self.back_ground = (0, 0, 0)
        self.window_size: Tuple[float, float] = (1024, 960)

    @abstractmethod
    async def update(self):
        pass

    @abstractmethod
    def init_view(self):
        # 初始化所有的关卡scene
        pass

    def get_behaviors(self) -> List[PyGameBehavior]:
        return sorted(list(self.behaviors.values()), key=lambda x: x.layer)

    @abstractmethod
    async def handle_event(self, operation: str):
        pass

