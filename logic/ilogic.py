from logic.system.isystem import ISystem
from typing import Dict
from logic.context import Context
from abc import abstractmethod
from common.logger import logger
import asyncio


class ILogic(object):
    LOGIC_RATE = 100e-3

    def __init__(self, gid: int, context: Context):
        self.gid: int = gid
        self.context: Context = context
        self.systems: Dict[str, ISystem] = {}
    
    def register_system(self, system: ISystem):
        system_name = system.__class__.__name__
        if system_name in self.systems:
            logger.debug("warning")
        self.systems[system_name] = system

    async def update(self):
        while True:
            for _, system in self.systems.items():
                await system.update()
            await asyncio.sleep(self.LOGIC_RATE)
    
    @abstractmethod
    def init_logic(self):
        pass
