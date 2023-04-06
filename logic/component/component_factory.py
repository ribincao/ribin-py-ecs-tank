from common.singleton import Singleton
from logic.component.transform_component import TransformComponent
from logic.component.move_component import MoveComponent
from logic.component.create_component import CreateComponent
from logic.component.box_collider_component import BoxColliderComponent
from logic.component.rigibody_component import RigibodyComponent
from logic.component.component import Component
from typing import Optional


class ComponentFactory(Singleton):

    def __init__(self):
        pass

    def get_component(self, component_name: str) -> Optional[Component]:
        if component_name == "transform":
            return TransformComponent()
        elif component_name == "create":
            return CreateComponent()
        elif component_name == "move":
            return MoveComponent()
        elif component_name == "box_collider":
            return BoxColliderComponent()
        elif component_name == "rigibody":
            return RigibodyComponent()
        else:
            return None


component_factory = ComponentFactory()


