from interface.game import IGame
from manager.context import Context
from typing import Dict

class TankGame(IGame):

    def __init__(self, gid: int):
        super(TankGame, self).__init__(gid)
        self.context: Context = Context()
    
    def init_game(self):
        from system.move_system import MoveSystem
        from system.create_system import CreateSystem
        from system.command_system import CommandSystem
        from system.collider_system import ColliderSystem
        
        self.register(MoveSystem(self.context))
        self.register(CreateSystem(self.context))
        self.register(CommandSystem(self.context))
        self.register(ColliderSystem(self.context))
    

