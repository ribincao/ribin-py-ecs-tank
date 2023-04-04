from typing import Tuple
from logic.component.component import Component


T_PLAYER = 'player'
T_ITEM = 'item'

class CreateComponent(Component):

    def __init__(self):
        super(CreateComponent, self).__init__()
        self.mod_name: str = ''
        self.mod_type: str = T_PLAYER


