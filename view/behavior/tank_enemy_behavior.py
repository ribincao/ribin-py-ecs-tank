from view.view import PyGameBehavior
from logic.entity.entity import GameLogicEntity


class TankEnemyBehavior(PyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankEnemyBehavior, self).__init__(entity)

    async def update(self):
        pass
