from common.singleton import Singleton
from logic.interface.system import System
from typing import Dict


class SystemManager(Singleton):

    def __init__(self):
        self._systems: Dict[str, System] = {}
    
    def register_system(self, system: System):
        system_name = system.__class__.__name__
        self._systems[system_name] = system

    def get_system(self) -> Dict[str, System]:
        return self._systems


system_manager = SystemManager()

