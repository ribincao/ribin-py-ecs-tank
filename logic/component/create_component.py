from typing import Tuple
from logic.component.icomponent import IComponent


class CreateComponent(IComponent):

    def __init__(self):
        self.mod_id: int = -1
        self.position: Tuple[float, float] = (0.0, 0.0)


