from view.view import PyGameBehavior
from logic.entity.entity import GameLogicEntity


class TankSymbolBehavior(PyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankSymbolBehavior, self).__init__(entity)

    async def update(self):
        pass
     
