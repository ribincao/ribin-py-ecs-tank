from logic.matrix.system import System
from logic.matrix.context import Context


class CommandSystem(System):

    def __init__(self, context: Context):
        super(CommandSystem, self).__init__(context)

    def update(self):
        commands = self.context.commands
        self.context.commands = []
        for command in commands:
            if command.uid < 0:
                continue
            command.execute(self.context.get_or_create_entity(command.uid))

