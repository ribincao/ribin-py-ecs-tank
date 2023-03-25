from interface.behavior import IBehavior
from interface.entity import IEntity


class TankBehavior(IBehavior):

    def __init__(self, entity: IEntity):
        super(TankBehavior, self).__init__(entity)


