from common.singleton import Singleton
from logic.interface.component import Component
from logic.component.transform_component import TransformComponent
from logic.component.move_component import MoveComponent
from logic.component.create_component import CreateComponent
from logic.component.box_collider_component import BoxColliderComponent
from logic.component.rigibody_component import RigibodyComponent
from logic.component.state_component import StateComponent
from logic.component.model_component import ModelComponent
from logic.component.player_component import PlayerComponent
from typing import Optional


class ComponentManager(Singleton):

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
        elif component_name == "model":
            return ModelComponent()
        elif component_name == "state":
            return StateComponent()
        elif component_name == "player":
            return PlayerComponent()
        else:
            return None


component_manager = ComponentManager()


