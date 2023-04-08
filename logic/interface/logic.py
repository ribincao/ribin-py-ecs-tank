from logic.interface.system import System
from logic.context import Context
from abc import abstractmethod
import asyncio
from logic.manager.system_manager import SystemManager


class Logic(object):
    LOGIC_RATE = 20e-3

    def __init__(self, gid: str, context: Context):
        self.gid: str = gid
        self.context: Context = context
        self.system_manager: SystemManager = SystemManager()
    
    def register_system(self, system: System):
        self.system_manager.register_system(system)

    async def update(self):
        for _, system in self.system_manager.get_system().items():
            await system.update()

    @abstractmethod
    def init_logic(self):
        pass
