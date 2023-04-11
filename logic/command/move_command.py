from logic.matrix.command import Command
from logic.matrix.entity import GameLogicEntity
from logic.component.state_component import State
from typing import Dict


class MoveDirection:
    STOP = -1
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


angel: Dict[int, float] = {
    MoveDirection.UP: 0,
    MoveDirection.LEFT: 90,
    MoveDirection.DOWN: 180,
    MoveDirection.RIGHT: 270
}


class MoveCmd(Command):

    def __init__(self, uid: int):
        super(MoveCmd, self).__init__(uid)
        self.direction: int = MoveDirection.STOP

    def execute(self, entity: GameLogicEntity):
        if not entity.get_component("move") or entity.get_component("move").speed <= 0:
            return
        if not entity.get_component("state"):
            return
        if MoveDirection.UP <= self.direction <= MoveDirection.RIGHT:
            entity.get_component("state").state = State.move
            entity.get_component("transform").rotation = angel.get(int(self.direction), 0)
        else:
            entity.get_component("state").state = State.normal
