from common.logger import logger
from logic.system.system import System
from logic.context import Context


class CommandSystem(System):

    def __init__(self, context: Context):
        super(CommandSystem, self).__init__(context)

    async def update(self):
        commands = self.context.commands
        self.context.commands = []
        for command in commands:
            if command.eid < 0:
                continue
            logger.debug(f"CommandSystem Update {command.__class__.__name__} {command.eid}")
            entity = self.context.get_entity(command.eid)
            await command.execute(entity)
