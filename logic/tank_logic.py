from logic.ilogic import ILogic
from logic.context import Context
from common.data_util import data_util
from common.logger import logger
from logic.component.transform_component import TransformComponent
from logic.component.create_component import CreateComponent
from logic.component.move_component import MoveComponent
from common.common import Vector2


class TankLogic(ILogic):

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
        maps = data_util.load_from_json('./view/scene/tank.json')
        logger.debug(f"logic_load_map {maps}")
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
                mod_name = item.get('mod_name', '')
                if not mod_name:
                    continue
                entity.add_create(mod_name)

                entity.mod_index = item.get('mod_index', 0)
                entity.layer = item.get('layer', 0)

                position = item.get('position', [0.0, 0.0])
                entity.add_transform(Vector2(position[0], position[1]))
                
                entity.add_move(5)
        

