from view.interface.view import PyGameBehavior
from logic.entity.entity import GameLogicEntity


class TankGrassBehavior(PyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankGrassBehavior, self).__init__(entity)

    async def update(self):
        pass
     
    def init_models(self):
        self._load_models("tank", "grass")