from interface.logic import ILogic
from interface.context import IContext
from common.data_util import data_util
from common.logger import logger
from logic.component.create_component import CreateComponent


class TankLogic(ILogic):

    def __init__(self, gid: int, context: IContext):
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
        idx = 1
        for map in maps:
            items = map.get("items", [])
            if not items:
                continue
            for item in items:
                entity = self.context.create_entity(idx)
                create_component = CreateComponent()
                create_component.__dict__.update(item)
                entity.create = create_component
        

