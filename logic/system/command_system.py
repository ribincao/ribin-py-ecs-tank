from common.logger import logger
from logic.interface.system import System
from logic.context import Context


class CommandSystem(System):

    def __init__(self, context: Context):
        super(CommandSystem, self).__init__(context)

    async def update(self):
        commands = self.context.commands
        self.context.commands = []
        for command in commands:
            if command.uid < 0:
                continue
            await command.execute(self.context.get_entity(command.uid))

