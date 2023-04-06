from logic.interface.command import Command
from logic.entity.entity import GameLogicEntity
from logic.component.state_component import State
from logic.component.move_component import MoveDirection


class MoveCmd(Command):

    def __init__(self, uid: int):
        super(MoveCmd, self).__init__(uid)
        self.direction = MoveDirection.STOP

    async def execute(self, entity: GameLogicEntity):
        if not entity.move or entity.move.speed <= 0:
            return
        if not entity.state:
            return
        if MoveDirection.UP <= self.direction <= MoveDirection.RIGHT:
            entity.state.state = State.move
            if entity.model:
                entity.model.model_index = self.direction
        else:
            entity.state.state = State.normal

