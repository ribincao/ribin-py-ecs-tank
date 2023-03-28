from view.behavior.ibehavior import IPyGameBehavior
from logic.entity.entity import GameLogicEntity
from common.logger import logger
import pygame.image as img


class TankBehavior(IPyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankBehavior, self).__init__(entity)

    def init_models(self, mod_id: int):
        from view.resource.gltf import GLTF
        gltf = GLTF()
        paths = gltf.load_models('tank', mod_id)
        logger.info(f"load_models {paths}")
        self.models = []
        for path in paths:
            self.models.append(img.load(path))


