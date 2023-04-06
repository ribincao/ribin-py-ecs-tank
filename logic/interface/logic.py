from logic.interface.system import System
from typing import Dict, List
from logic.context import Context
from abc import abstractmethod
from common.logger import logger
import asyncio
from common.data_util import data_util


class Logic(object):
    LOGIC_RATE = 20e-3

    def __init__(self, gid: str, context: Context):
        self.gid: str = gid
        self.context: Context = context
        self.systems: Dict[str, System] = {}
        self.gltf = []
    
    def register_system(self, system: System):
        system_name = system.__class__.__name__
        if system_name in self.systems:
            logger.debug("warning")
        self.systems[system_name] = system

    async def update(self):
        while True:
            for _, system in self.systems.items():
                await system.update()
            await asyncio.sleep(self.LOGIC_RATE)

    def get_models(self, mod_name: str):
        if not self.gltf:
            self.gltf = data_util.load_from_json(f'./view/resource/{self.gid}/gltf.json')
        if not self.gltf:
            return []
        for data in self.gltf:
            _mod_name = data.get('mod_name', '')
            if _mod_name != mod_name:
                continue
            return data.get('models', [])
        return []
    
    @abstractmethod
    def init_logic(self):
        pass
