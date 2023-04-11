from logic.matrix.ilogic import Logic
from logic.matrix.context import Context
from common.data_util import data_util
from common.logger import logger
from logic.command.create_command import CreateCmd


class TankLogic(Logic):

    def __init__(self, gid: str, context: Context):
        super(TankLogic, self).__init__(gid, context)
    
    def init_logic(self):
        from logic.system.move_system import MoveSystem
        from logic.system.command_system import CommandSystem
        from logic.system.collider_system import ColliderSystem
        from logic.system.destroy_system import DestroySystem
        from logic.system.enemy_system import EnemySystem
        from logic.system.create_system import CreateSystem
        
        self.register_system(CreateSystem(self.context))
        self.register_system(CommandSystem(self.context))
        self.register_system(MoveSystem(self.context))
        self.register_system(ColliderSystem(self.context))
        self.register_system(EnemySystem(self.context))
        self.register_system(DestroySystem(self.context))

        self.load_map(f"./view/scene/{self.gid}.json")

    def load_map(self, path: str):
        # 场景重建
        scene = data_util.load_from_json(path)
        logger.debug(f"logic_load_map {map}")
        if not scene:
            return
        items = scene.get("items", [])
        self.context.edge_size = scene.get("window_size", [780, 780])
        for item in items:
            is_async = item.get("is_async", True)
            entity = self.context.create_entity(is_async)

            cmd = CreateCmd(entity.uid)
            cmd.node_data = item
            self.context.input_command(cmd)


