from view.interface.pygame_behavior import PyGameBehavior
from logic.entity.entity import GameLogicEntity


class TankPlayerBehavior(PyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankPlayerBehavior, self).__init__(entity)

    def update(self):
        pass

    def init_models(self):
        self.models = self._load_models("tank", "player")
