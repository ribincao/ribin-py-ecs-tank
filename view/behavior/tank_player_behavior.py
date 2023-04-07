from view.interface.behavior import PyGameBehavior
from logic.entity.entity import GameLogicEntity
from typing import Tuple


class TankPlayerBehavior(PyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankPlayerBehavior, self).__init__(entity)

    def get_bullet_position(self) -> Tuple[float, float]:
        position = self.entity.transform.position
        if not self.entity.model or not self.rect:
            return 0, 0

        if self.entity.transform.rotation == 0:
            return position[0], position[1] - self.rect.height / 2
        elif self.entity.transform.rotation == 180:
            return position[0], position[1] + self.rect.height / 2
        elif self.entity.transform.rotation == 90:
            return position[0] - self.rect.width / 2, position[1]
        elif self.entity.transform.rotation == 270:
            return position[0] + self.rect.width / 2, position[1]

        return 0.0, 0.0

    async def update(self):
        pass

    def init_models(self):
        from view.resource.gltf import GLTF
        import pygame.image as img
        gltf = GLTF()
        models = gltf.load_models("tank", "player")
        self.models = {}
        for model in models:
            model_index = model.get("model_index", '')
            if not model_index:
                continue
            path = model.get("model", "")
            if not path:
                continue
            self.models[model_index] = img.load(path)

