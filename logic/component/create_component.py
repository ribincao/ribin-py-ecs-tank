from typing import Tuple
from logic.component.icomponent import IComponent


T_PLAYER = 'player'
T_ITEM = 'item'

class CreateComponent(IComponent):

    def __init__(self):
        super(CreateComponent, self).__init__()
        self.mod_id: int = -1
        self.mod_type: str = T_PLAYER


