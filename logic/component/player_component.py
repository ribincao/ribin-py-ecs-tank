from logic.interface.component import Component


class PlayerComponent(Component):

    def __init__(self, is_async: bool = True):
        super(PlayerComponent, self).__init__(is_async)
        self.player_id: str = ''

