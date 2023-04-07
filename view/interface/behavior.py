from logic.entity.entity import GameLogicEntity
from typing import Dict, Tuple
from abc import abstractmethod
from view.resource.gltf import GLTF


class Behavior(object):

    def __init__(self, entity: GameLogicEntity):
        self.entity: GameLogicEntity = entity
        self.models: Dict[str, object] = {}
        self.gltf: GLTF = GLTF()

    @property
    def uid(self):
        return self.entity.uid

    @abstractmethod
    def init_models(self):
        pass

    @abstractmethod
    async def update(self):
        pass

    @abstractmethod
    def mode(self) -> object:
        pass

    @abstractmethod
    def rect(self) -> object:
        pass
    
    def get_forward(self) -> Tuple[Tuple[float, float], float]:
        return (0.0, 0.0), 0.0



