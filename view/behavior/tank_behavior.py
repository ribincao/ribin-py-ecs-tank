from view.behavior.ibehavior import IPyGameBehavior
from logic.entity.entity import GameLogicEntity


class TankBehavior(IPyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankBehavior, self).__init__(entity)

    def init_modes(self):
        pass


