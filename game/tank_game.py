from interface.game import IGame


class TankGame(IGame):

    def __init__(self, gid: int):
        super(TankGame, self).__init__(gid)


