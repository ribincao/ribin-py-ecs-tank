from common.logger import logger
from logic.system.isystem import ISystem
from logic.context import Context


class CommandSystem(ISystem):

    def __init__(self, context: Context):
        super(CommandSystem, self).__init__(context)

    async def update(self):
        logger.debug("CommandSystem Update")
        commands = self.context.commands
        self.context.commands = []
        for command in commands:
            entity = self.context.get_entity(command.eid)
            if not entity:
                continue
            await command.execute(entity)
