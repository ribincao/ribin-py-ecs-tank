from interface.entity import IEntity
from component.transform_component import TransformComponent


class TankPlayer(IEntity):

    def __init__(self, uid: int):
        super(TankPlayer, self).__init__(uid)
        self.transform: TransformComponent = TransformComponent() 

