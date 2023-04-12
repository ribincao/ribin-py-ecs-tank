from logic.matrix.command import Command
from logic.logic_entity import GameLogicEntity
from logic.component.create_component import CreateComponent


class CreateCmd(Command):

    def __init__(self, uid: int):
        super(CreateCmd, self).__init__(uid)
        self.node_data: dict = {}

    def execute(self, entity: GameLogicEntity):
        comp = CreateComponent()
        comp.node_data = self.node_data
        entity.add_component(comp)

