from interface.game import IGame
from interface.context import IContext


class TankGame(IGame):

    def __init__(self, gid: int, context: IContext):
        super(TankGame, self).__init__(gid, context)
    
    def init_system(self):
        from system.move_system import MoveSystem
        from system.create_system import CreateSystem
        from system.command_system import CommandSystem
        from system.collider_system import ColliderSystem
        
        self.register_system(MoveSystem(self.context))
        self.register_system(CreateSystem(self.context))
        self.register_system(CommandSystem(self.context))
        self.register_system(ColliderSystem(self.context))
    

