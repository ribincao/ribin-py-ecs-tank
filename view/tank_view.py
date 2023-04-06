from view.view import View
from logic.context import Context
from common.logger import logger
from logic.entity.entity import GameLogicEntity
from view.behavior.tank_behavior import TankBehavior
from common.data_util import data_util
import asyncio
from logic.component.move_component import MoveDirection
from logic.manager.command_manager import command_manager
from logic.interface.command import Command
from typing import Optional, Tuple
from logic.component.state_component import State
from view.manager.behavior_manager import behavior_manager


class TankView(View):
    MODULE = 'tank'

    def __init__(self, context: Context):
        super(TankView, self).__init__(context)
        self.player_uid: int = 0
        self.window_size: Tuple[float, float] = (780, 780)

    async def update(self):
        while True:
            behaviors = {}
            for entity in self.context.get_entities():
                behavior = self.behaviors.get(entity.uid, None)
                if not behavior:
                    behavior = self.create_behavior(entity)
                behavior.entity = entity
                behaviors[entity.uid] = behavior
                await behavior.update()
            self.behaviors = behaviors
            await asyncio.sleep(self.VIEW_RATE)

    def create_behavior(self, entity: GameLogicEntity):
        behavior = behavior_manager.get_tank_behavior(entity)
        if entity.model:
            behavior.init_models(self.MODULE, entity.model.model_name)
        self.behaviors[entity.uid] = behavior
        return behavior

    def init_view(self):
        map = data_util.load_from_json('./view/scene/tank.json')
        logger.debug(f"view_load_tank_scene {map}")
        if map:
            self.window_size = map.get("window_size", [780, 780])
    
    async def handle_event(self, operation: str):

        cmd: Optional[Command] = None
        if operation == 'w' and self.player_uid:
            cmd = command_manager.get_move_cmd(self.player_uid, MoveDirection.UP)
        elif operation == 'a' and self.player_uid:
            cmd = command_manager.get_move_cmd(self.player_uid, MoveDirection.LEFT)
        elif operation == 's' and self.player_uid:
            cmd = command_manager.get_move_cmd(self.player_uid, MoveDirection.DOWN)
        elif operation == 'd' and self.player_uid:
            cmd = command_manager.get_move_cmd(self.player_uid, MoveDirection.RIGHT)
        elif operation == '-' and self.player_uid:
            cmd = command_manager.get_move_cmd(self.player_uid, MoveDirection.STOP)

        elif operation == 'n' and self.player_uid <= 0:
            entity = self.context.create_entity()
            node_data = {
                    "state": {"state": State.normal},
                    "move": {"speed": 5},
                    "model": {"model_name": "player1"},
                    "box_collider": {"layer": 1, "width": 60, "height": 60},
                    "transform": {"position": (285.0, 720.0)}
            }
            cmd = command_manager.get_create_cmd(entity.uid, node_data)
            self.player_uid = entity.uid
        elif operation == 'm' and self.player_uid <= 0:
            entity = self.context.create_entity()
            node_data = {
                    "state": {"state": State.normal},
                    "move": {"speed": 5},
                    "model": {"model_name": "player2"},
                    "box_collider": {"layer": 1, "width": 60, "height": 60},
                    "transform": {"position": (435.0, 720.0)}
            }
            cmd = command_manager.get_create_cmd(entity.uid, node_data)
            self.player_uid = entity.uid

        elif operation == 'j' and self.player_uid > 0:
            tank = self.behaviors.get(self.player_uid)
            if not tank or not tank.entity.model:
                return
            entity = self.context.create_entity()
            node_data = {
                    "move": {"speed": 5},
                    "model": {"model_name": "bullet", "model_index": tank.entity.model.model_index},
                    "box_collider": {"layer": 1, "width": 12, "height": 12},
                    "transform": {"position": tank.get_bullet_position()},
                    "state": {"state": State.move}
            }
            cmd = command_manager.get_create_cmd(entity.uid, node_data)

        self.send_cmd(cmd)
        
    def send_cmd(self, cmd: Optional[Command]):
        if not cmd:
            return
        self.context.input_command(cmd)
        if self.context.is_connected:
            self.context.input_message(cmd)

