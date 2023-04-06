from logic.interface.command import Command
from logic.entity.entity import GameLogicEntity


class CreateCmd(Command):

    def __init__(self, uid: int):
        super(CreateCmd, self).__init__(uid)
        self.node_data: dict = {}

    async def execute(self, entity: GameLogicEntity):
        entity.add_create(False, self.node_data)

