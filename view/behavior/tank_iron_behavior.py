from view.interface.pygame_behavior import PyGameBehavior
from logic.entity.entity import GameLogicEntity


class TankIronBehavior(PyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankIronBehavior, self).__init__(entity)

    async def update(self):
        pass
     
    def init_models(self):
        self._load_models("tank", "iron")
