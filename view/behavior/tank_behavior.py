from interface.behavior import IPyGameBehavior
from interface.entity import IEntity


class TankBehavior(IPyGameBehavior):

    def __init__(self, entity: IEntity):
        super(TankBehavior, self).__init__(entity)

    def init_modes(self):
        pass


