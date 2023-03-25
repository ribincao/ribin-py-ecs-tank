from interface.system import ISystem
from interface.context import IContext
from typing import Dict


class SystemManager(object):

    def __init__(self, context: IContext):
        self.context: IContext = context
        self.systems: Dict[str, ISystem] = {}

    def register_system(self, system: ISystem):
        system_name = system.__class__.__name__
        if system_name in self.systems:
            print(f"warning: {system_name} already exist.")

    def init_system(self):
        from system.collider_system import ColliderSystem
        from system.create_system import CreateSystem
        from system.command_system import CommandSystem
        from system.move_system import MoveSystem

        self.register_system(ColliderSystem(self.context))
        self.register_system(CreateSystem(self.context))
        self.register_system(CommandSystem(self.context))
        self.register_system(MoveSystem(self.context))


