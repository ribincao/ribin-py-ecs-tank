from logic.command.move_command import MoveCmd
from logic.command.create_command import CreateCmd
from common.singleton import Singleton
from logic.interface.command import Command
from typing import Optional
import json


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


command_manager = CommandManager()

