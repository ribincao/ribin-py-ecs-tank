from logic.logic import Logic
from logic.context import Context
from common.data_util import data_util
from common.logger import logger
from common.common import Vector2
from logic.command.create_command import CreateCmd


class TankLogic(Logic):

    def __init__(self, gid: str, context: Context):
        super(TankLogic, self).__init__(gid, context)
    
    def init_logic(self):
        from logic.system.move_system import MoveSystem
        from logic.system.command_system import CommandSystem
        from logic.system.collider_system import ColliderSystem
        
        self.register_system(MoveSystem(self.context))
        self.register_system(CommandSystem(self.context))
        self.register_system(ColliderSystem(self.context))

        # 场景重建
        map = data_util.load_from_json('./view/scene/tank.json')
        logger.debug(f"logic_load_map {map}")
        if not map:
            return
        items = map.get("items", [])
        for item in items:
            entity = self.context.create_entity()
            cmd = CreateCmd(entity.uid)
            cmd.__dict__.update(item)
            self. context.input_command(cmd)
        logger.info(f"{self.context.uid_cnt} entity created.")
        

