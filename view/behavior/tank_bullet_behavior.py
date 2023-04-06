from view.interface.view import PyGameBehavior
from logic.entity.entity import GameLogicEntity


class TankBulletBehavior(PyGameBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(TankBulletBehavior, self).__init__(entity)

    async def update(self):
        pass
