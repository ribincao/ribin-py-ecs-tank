from interface.system import ISystem
from interface.context import IContext


class CreateSystem(ISystem):

    def __init__(self, context: IContext):
        super(CreateSystem, self).__init__(context)

    async def update(self):
        pass
