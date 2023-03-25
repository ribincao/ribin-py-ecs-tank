from interface.system import ISystem
from interface.context import IContext


class ColliderSystem(ISystem):

    def __init__(self, context: IContext):
        super(ColliderSystem, self).__init__(context)

    async def update(self):
        pass
