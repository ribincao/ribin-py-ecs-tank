from logic.matrix.entity import Entity
from logic.manager.component_manager import *


class GameLogicEntity(Entity):

    def __init__(self):
        super(GameLogicEntity, self).__init__()

    @property
    def transform(self) -> Optional[TransformComponent]:
        return self.get_component("transform")

    @property
    def create(self) -> Optional[CreateComponent]:
        return self.get_component("create")

    @property
    def model(self) -> Optional[ModelComponent]:
        return self.get_component("model")

    @property
    def move(self) -> Optional[MoveComponent]:
        return self.get_component("move")

    @property
    def box2d_collider(self) -> Optional[BoxColliderComponent]:
        return self.get_component("box2d_collider")

    @property
    def bullet(self) -> Optional[BulletComponent]:
        return self.get_component("bullet")

    @property
    def state(self) -> Optional[StateComponent]:
        return self.get_component("state")
