from logic.command.move_command import MoveCmd
from logic.command.create_command import CreateCmd
from common.singleton import Singleton
from logic.matrix.command import Command
from typing import Optional
import json
from view.interface.pygame_behavior import PyGameBehavior
from logic.component.state_component import State
import random


class CommandManager(Singleton):

    def __init__(self):
        pass

    def from_dict(self, d: dict) -> Optional[Command]:
        command_name = d.get('name', '')
        if not command_name:
            return None
        uid = d.get('uid', -1)
        if uid < 0:
            return None

        cmd = None
        if command_name == 'move':
            cmd = MoveCmd(uid)
            cmd.__dict__.update(d)
        if command_name == 'create':
            cmd = CreateCmd(uid)
            cmd.__dict__.update(d)
        return cmd

    def create_cmd(self, s: str) -> Optional[Command]:
        d = json.loads(s)
        return self.from_dict(d)

    @staticmethod
    def get_move_cmd(uid: int, direction: int) -> MoveCmd:
        cmd = MoveCmd(uid)
        cmd.direction = direction
        return cmd

    @staticmethod
    def get_create_cmd(uid: int, node_data: dict) -> CreateCmd:
        cmd = CreateCmd(uid)
        cmd.node_data = node_data
        return cmd

    def create_tank_player_cmd(self, uid: int, player_id: str, is_player1: bool = True) -> CreateCmd:
        node_data = {
            "state": {"state": State.normal},
            "move": {"speed": 5},
            "model": {"model_name": "player", "model_index": "player1" if is_player1 else "player2"},
            "boxcollider": {"layer": 1, "width": 60, "height": 60},
            "transform": {"position": (310.0, 750.0) if is_player1 else (470.0, 750.0)},
            "player": {"player_id": player_id}
        }
        cmd = self.get_create_cmd(uid, node_data)
        return cmd
    
    def tank_shot_cmd(self, uid: int, tank: PyGameBehavior) -> CreateCmd:
        position, rotation = tank.get_forward()
        node_data = {
                "move": {"speed": 5},
                "model": {"model_name": "bullet", "model_index": "bullet"},
                "boxcollider": {"layer": 1, "width": 12, "height": 12},
                "transform": {"position": position, "rotation": rotation},
                "state": {"state": State.move},
                "bullet": {"belong": tank.entity.uid}
        }
        cmd = self.get_create_cmd(uid, node_data)
        return cmd

    def create_tank_enemy_cmd(self, uid: int) -> CreateCmd:
        positions = [(30, 30), (390, 30), (750, 30)]
        model_index = ["enemy" + str(i) for i in range(1, 7)]
        node_data = {
            "state": {"state": State.move},
            "move": {"speed": 2},
            "model": {"model_name": "enemy", "model_index": random.choice(model_index)},
            "boxcollider": {"layer": 1, "width": 60, "height": 60},
            "transform": {"position": random.choice(positions), "rotation": 180.0},
        }
        cmd = self.get_create_cmd(uid, node_data)
        return cmd


command_manager = CommandManager()

