from logic.command.icommand import ICommand


class MoveCmd(ICommand):

    def __init__(self, eid: int):
        super(MoveCmd, self).__init__(eid)

    def execute(self):
        pass
