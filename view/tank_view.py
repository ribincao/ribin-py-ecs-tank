from interface.view import IView
from interface.context import IContext


class TankView(IView):

    def __init__(self, context: IContext):
        super(TankView, self).__init__(context)

    def init_view(self):
        pass
