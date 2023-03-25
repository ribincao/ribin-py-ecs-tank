from interface.system import ISystem
from typing import Dict
from interface.context import IContext


class IGame(object):

    def __init__(self, gid: int, context: IContext):
        self.gid: int = gid
        self.context: IContext = context
        self.systems: Dict[str, ISystem] = {}
    
    def register_system(self, system: ISystem):
        system_name = system.__class__.__name.__
        if system_name in self.systems:
            print("warning")
        self.systems[system_name] = system

    def update(self):
        for _, system in self.systems.items():
            system.update()
