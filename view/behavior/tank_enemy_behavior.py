from view.interface.pygame_behavior import PyGameBehavior
from logic.entity.entity import GameLogicEntity


class TankEnemyBehavior(PyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankEnemyBehavior, self).__init__(entity)

    def update(self):
        pass
    
    def init_models(self):
        self._load_models("tank", "enemy")
