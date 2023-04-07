from view.interface.view import PyGameBehavior
from logic.entity.entity import GameLogicEntity


class TankWaterBehavior(PyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankWaterBehavior, self).__init__(entity)

    async def update(self):
        pass
     
    def init_models(self):
        from view.resource.gltf import GLTF
        import pygame.image as img
        gltf = GLTF()
        models = gltf.load_models("tank", "water")
        self.models = {}
        for model in models:
            model_index = model.get("model_index", '')
            if not model_index:
                continue
            path = model.get("model", "")
            if not path:
                continue
            self.models[model_index] = img.load(path)
