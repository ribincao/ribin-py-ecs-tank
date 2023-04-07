from logic.context import Context
from abc import abstractmethod
from typing import List, Dict, Tuple
from view.interface.pygame_behavior import PyGameBehavior
from view.interface.view import View
import asyncio
from logic.entity.entity import GameLogicEntity
from view.manager.behavior_manager import behavior_manager
from common.data_util import data_util


class PyGameView(View):

    def __init__(self, context: Context):
        super(PyGameView, self).__init__(context)
        self.behaviors: Dict[int, PyGameBehavior] = {}
        self.back_ground = (0, 0, 0)
        self.window_size: Tuple[float, float] = (1024, 960)

    async def update(self):
        while True:
            behaviors = {}
            for entity in self.context.get_entities():
                if not entity.model:
                    continue
                behavior = self.behaviors.get(entity.uid, None)
                if not behavior:
                    behavior = self.create_behavior(entity)
                behavior.entity = entity
                behaviors[entity.uid] = behavior
                await behavior.update()
            self.behaviors = behaviors
            await asyncio.sleep(self.VIEW_RATE)

    def create_behavior(self, entity: GameLogicEntity):
        behavior = behavior_manager.get_tank_behavior(entity)
        behavior.init_models()
        self.behaviors[entity.uid] = behavior
        return behavior

    def init_view(self):
        scene = data_util.load_from_json('./view/scene/tank.json')
        if scene:
            self.window_size = scene.get("window_size", [780, 780])

    def get_behaviors(self) -> List[PyGameBehavior]:
        return sorted(list(self.behaviors.values()), key=lambda x: x.layer)

    @abstractmethod
    async def handler(self, operation: str):
        pass

