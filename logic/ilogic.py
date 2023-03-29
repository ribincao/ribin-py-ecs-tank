from logic.system.isystem import ISystem
from typing import Dict, List
from logic.context import Context
from abc import abstractmethod
from common.logger import logger
import asyncio
from common.data_util import data_util


class ILogic(object):
    LOGIC_RATE = 100e-3

    def __init__(self, gid: str, context: Context):
        self.gid: str = gid
        self.context: Context = context
        self.systems: Dict[str, ISystem] = {}
        self.gltf: List[dict] = []
    
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

    def get_models(self, mod_id: int):
        if not self.gltf:
            self.gltf = data_util.load_from_json(f'./view/resource/{self.gid}/gltf.json')
        if not self.gltf:
            return []
        for data in self.gltf:
            _mod_id = data.get('mod_id', -1)
            if _mod_id != mod_id:
                continue
            return data.get('models', [])
        return []
    
    @abstractmethod
    def init_logic(self):
        pass
