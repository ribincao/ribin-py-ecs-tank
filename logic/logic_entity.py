from logic.matrix.entity import Entity
from logic.manager.component_manager import *


class GameLogicEntity(Entity):

    def __init__(self):
        super(GameLogicEntity, self).__init__()

    @property
    def transform(self) -> Optional[TransformComponent]:
        return self._get_component("transform")

    @property
    def create(self) -> Optional[CreateComponent]:
        return self._get_component("create")

    @property
    def model(self) -> Optional[ModelComponent]:
        return self._get_component("model")

    @property
    def move(self) -> Optional[MoveComponent]:
        return self._get_component("move")

    @property
    def box2d_collider(self) -> Optional[BoxColliderComponent]:
        return self._get_component("box2d_collider")

    @property
    def bullet(self) -> Optional[BulletComponent]:
        return self._get_component("bullet")

    @property
    def state(self) -> Optional[StateComponent]:
        return self._get_component("state")

    @property
    def player(self) -> Optional[PlayerComponent]:
        return self._get_component("player")

    @property
    def rigibody(self) -> Optional[RigibodyComponent]:
        return self._get_component("rigibody")
