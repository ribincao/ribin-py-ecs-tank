from interface.system import ISystem
from typing import Dict


class IGame(object):

    def __init__(self, gid: int):
        self.gid: int = gid
        self.systems: Dict[str, ISystem] = {}
    
    def register_system(self, system: ISystem):
        system_name = system.__class__.__name.__
        if system_name in self.systems:
            print("warning")
        self.systems[system_name] = system

    def update(self):
        for _, system in self.systems.items():
            system.update()
