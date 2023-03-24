from interface.entity import IEntity
from component.transform_component import TranformComponent 


class TankPlayer(IEntity):

    def __init__(self, uid: int):
        super(TankEntity, self).__init__(uid)
        self.transform: TransformComponent = TransformComponent() 

