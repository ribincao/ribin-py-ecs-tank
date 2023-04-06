from view.interface.view import PyGameBehavior
from logic.entity.entity import GameLogicEntity


class TankWallBehavior(PyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankWallBehavior, self).__init__(entity)

    async def update(self):
        pass
     
