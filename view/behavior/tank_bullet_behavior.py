from view.interface.pygame_behavior import PyGameBehavior
from logic.entity.entity import GameLogicEntity


class TankBulletBehavior(PyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankBulletBehavior, self).__init__(entity)

    def update(self):
        pass
    
    def init_models(self):
        self._load_models("tank", "bullet")
