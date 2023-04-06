from view.interface.view import PyGameBehavior
from logic.entity.entity import GameLogicEntity


class TankSteelBehavior(PyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankSteelBehavior, self).__init__(entity)

    async def update(self):
        pass
     
