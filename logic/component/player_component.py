from logic.interface.component import Component


class PlayerComponent(Component):

    def __init__(self):
        super(PlayerComponent, self).__init__()
        self.player_id: str = ''

