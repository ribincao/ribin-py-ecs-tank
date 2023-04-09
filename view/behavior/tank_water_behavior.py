from view.interface.pygame_behavior import PyGameBehavior
from logic.entity.entity import GameLogicEntity


class TankWaterBehavior(PyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankWaterBehavior, self).__init__(entity)

    def update(self):
        pass
     
    def init_models(self):
        self.models = self._load_models("tank", "water")
