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
        class_name = d.get('__class__', '')
        if not class_name:
            return None
        uid = d.get('uid', -1)
        if uid < 0:
            return None

        cmd = None
        if class_name == 'MoveCmd':
            cmd = MoveCmd(uid)
            cmd.__dict__.update(d)
        if class_name == 'CreateCmd':
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
    def get_create_cmd(uid: int, d: dict) -> CreateCmd:
        cmd = CreateCmd(uid)
        cmd.__dict__.update(d)
        return cmd


command_manager = CommandManager()
