from view.behavior.ibehavior import IPyGameBehavior
from logic.entity.entity import GameLogicEntity
from common.logger import logger
import pygame.image as img


class TankBehavior(IPyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankBehavior, self).__init__(entity)


