from view.view import View
from logic.context import Context
from common.logger import logger
from logic.entity.entity import GameLogicEntity
from view.behavior.tank_behavior import TankBehavior
from common.data_util import data_util
import asyncio
from logic.command.move_command import UP, DOWN, LEFT, RIGHT, STOP
from logic.command.command_factory import cmd_factory
from logic.command.command import Command
from typing import Optional, Tuple
from logic.entity.state import EntityState


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
        behavior = TankBehavior(entity)

        if entity.create:
            behavior.init_models(self.MODULE, entity.create.mod_name)
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
            cmd = cmd_factory.get_move_cmd(self.player_uid, UP)
        elif operation == 'a' and self.player_uid:
            cmd = cmd_factory.get_move_cmd(self.player_uid, LEFT)
        elif operation == 's' and self.player_uid:
            cmd = cmd_factory.get_move_cmd(self.player_uid, DOWN)
        elif operation == 'd' and self.player_uid:
            cmd = cmd_factory.get_move_cmd(self.player_uid, RIGHT)
        elif operation == '-' and self.player_uid:
            cmd = cmd_factory.get_move_cmd(self.player_uid, STOP)

        elif operation == 'n' and self.player_uid <= 0:
            entity = self.context.create_entity()
            d = {
                    "speed": 5,
                    "mod_name": "player1",
                    "layer": 1,
                    "position": [285.0, 720.0]
            }
            cmd = cmd_factory.get_create_cmd(entity.uid, d)
            self.player_uid = entity.uid
        elif operation == 'm' and self.player_uid <= 0:
            entity = self.context.create_entity()
            d = {
                    "speed": 5,
                    "mod_name": "player2",
                    "layer": 1,
                    "position": [435.0, 720.0]
            }
            cmd = cmd_factory.get_create_cmd(entity.uid, d)
            self.player_uid = entity.uid

        elif operation == 'j' and self.player_uid > 0:
            tank = self.behaviors.get(self.player_uid)
            if not tank:
                return
            entity = self.context.create_entity()
            d = {
                    "mod_index": tank.entity.mod_index,
                    "state": EntityState.move,
                    "speed": 5,
                    "mod_name": "bullet",
                    "layer": 1,
                    "position": tank.get_bullet_position()
            }
            cmd = cmd_factory.get_create_cmd(entity.uid, d)

        self.send_cmd(cmd)
        
    def send_cmd(self, cmd: Optional[Command]):
        if not cmd:
            return
        self.context.input_command(cmd)
        if self.context.is_connected:
            self.context.input_message(cmd)

