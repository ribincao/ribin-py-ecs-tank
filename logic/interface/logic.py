from logic.interface.system import System
from logic.context import Context
from abc import abstractmethod
import asyncio
from common.data_util import data_util
from logic.manager.system_manager import SystemManager


class Logic(object):
    LOGIC_RATE = 20e-3

    def __init__(self, gid: str, context: Context):
        self.gid: str = gid
        self.context: Context = context
        self.system_manager: SystemManager = SystemManager()
        self.gltf = []
    
    def register_system(self, system: System):
        self.system_manager.register_system(system)

    async def update(self):
        while True:
            for _, system in self.system_manager.get_system().items():
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
