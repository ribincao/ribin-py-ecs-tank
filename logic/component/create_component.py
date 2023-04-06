from logic.interface.component import Component


class EntityType:
    T_PLAYER = 'player'
    T_ITEM = 'item'


class CreateComponent(Component):

    def __init__(self):
        super(CreateComponent, self).__init__()
        self.mod_name: str = ''
        self.mod_type: str = EntityType.T_ITEM
        self.create_status: bool = False
        self.node_data: dict = {}


