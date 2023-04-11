from logic.matrix.context import Context
from abc import abstractmethod
from typing import List, Dict, Tuple
from view.interface.iview import View
from logic.matrix.entity import GameLogicEntity
from common.data_util import data_util
from view.interface.pygame_behavior import PyGameBehavior
from view.manager.animation_manager import Animation


class PyGameView(View):

    def __init__(self, gid: str, context: Context):
        super(PyGameView, self).__init__(gid, context)
        self.behaviors: Dict[int, PyGameBehavior] = {}
        self.animations: List[Animation] = []
        self.back_ground = (0, 0, 0)
        self.window_size: Tuple[float, float] = (1024, 960)

    def update(self):
        behaviors = {}
        for entity in self.context.entities:
            if not entity.get_component("model"):
                continue
            behavior = self.behaviors.get(entity.uid, None)
            if not behavior:
                behavior = self.create_behavior(entity)
            behavior.entity = entity
            behaviors[entity.uid] = behavior
            behavior.update()
        self.behaviors = behaviors

        animations = []
        for animation in self.animations:
            model, rect = animation.animation
            if not model or not rect:
                continue
            animations.append(animation)
        self.animations = animations

    def create_behavior(self, entity: GameLogicEntity):
        behavior = PyGameBehavior(entity)
        behavior.init_models(self.gid)
        self.behaviors[entity.uid] = behavior
        return behavior

    def init_view(self):
        scene = data_util.load_from_json(f'./view/scene/{self.gid}.json')
        if scene:
            self.window_size = scene.get("window_size", [780, 780])

    def get_behaviors(self) -> List[PyGameBehavior]:
        return sorted(list(self.behaviors.values()), key=lambda x: x.layer)

    @abstractmethod
    def handler(self, operation: str):
        pass
