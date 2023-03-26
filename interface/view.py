from interface.context import IContext
from abc import abstractmethod
from typing import List, Dict
from interface.behavior import IPyGameBehavior, IBehavior
from interface.entity import IEntity


class IView(object):
    VIEW_RATE = 100e-3

    def __init__(self, context: IContext):
        self.behaviors: Dict[int, IBehavior] = {}
        self.context: IContext = context
        self.scenes: Dict[str, object] = {}
        self.scene_id: str = ""  # 场景id, 不同关卡
        self.back_ground = (0, 0, 0)

    async def update(self):
        behaviors = {}
        for entity in self.context.get_entities():
            behavior = self.create_behavior(entity)
            behaviors[entity.uid] = behavior
        self.behaviors = behaviors

    @abstractmethod
    def init_view(self):
        # 初始化所有的关卡scene
        pass

    def get_behaviors(self) -> List[IBehavior]:
        return list(self.behaviors.values())

    def create_behavior(self, entity: IEntity):
        if entity.uid in self.behaviors:
            self.behaviors[entity.uid].entity = entity
            return self.behaviors[entity.uid]
        behavior = IPyGameBehavior(entity)  # todo: 根据类型创建不同的behavior
        self.behaviors[entity.uid] = behavior
        return behavior

    @abstractmethod
    async def handle_event(self, operation: str):
        pass

