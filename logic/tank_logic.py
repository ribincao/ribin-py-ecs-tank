from logic.ilogic import ILogic
from logic.context import Context
from common.data_util import data_util
from common.logger import logger
from logic.component.transform_component import TransformComponent
from logic.component.create_component import CreateComponent
from common.common import Vector2


class TankLogic(ILogic):

    def __init__(self, gid: int, context: Context):
        super(TankLogic, self).__init__(gid, context)
    
    def init_logic(self):
        from logic.system.move_system import MoveSystem
        from logic.system.create_system import CreateSystem
        from logic.system.command_system import CommandSystem
        from logic.system.collider_system import ColliderSystem
        
        self.register_system(MoveSystem(self.context))
        self.register_system(CreateSystem(self.context))
        self.register_system(CommandSystem(self.context))
        self.register_system(ColliderSystem(self.context))

        # 场景重建
        maps = data_util.load_from_json('./view/scene/tank.json')
        logger.info(f"logic_load_map {maps}")
        if not maps:
            return
        for map in maps:
            items = map.get("items", [])
            if not items:
                continue
            for item in items:
                idx = item.get('uid', -1)
                if idx < 0:
                    continue
                entity = self.context.create_entity(idx)
                position = item.get('position', [0.0, 0.0])
                transform_comp = TransformComponent()
                transform_comp.position = Vector2(position[0], position[1])
                entity.transform = transform_comp
                mod_id = item.get('mod_id', 0)
                create_comp = CreateComponent()
                create_comp.mod_id = mod_id
                entity.create = create_comp
                
        

