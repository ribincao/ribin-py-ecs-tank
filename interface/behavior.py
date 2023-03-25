from interface.entity import IEntity


class IBehavior(object):

    def __init__(self, entity: IEntity):
        self.entity: IEntity = entity
        self.model = None

    def set_mode(self, mode):
        self.mode = mode


