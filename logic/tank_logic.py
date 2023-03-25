from interface.logic import ILogic
from interface.context import IContext


class TankLogic(ILogic):

    def __init__(self, gid: int, context: IContext):
        super(TankLogic, self).__init__(gid, context)
    
    def init_logic(self):
        from system.move_system import MoveSystem
        from system.create_system import CreateSystem
        from system.command_system import CommandSystem
        from system.collider_system import ColliderSystem
        
        self.register_system(MoveSystem(self.context))
        self.register_system(CreateSystem(self.context))
        self.register_system(CommandSystem(self.context))
        self.register_system(ColliderSystem(self.context))
    

