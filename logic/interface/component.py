

class Component(object):

    def __init__(self, is_async: bool = True):
        self.is_async: bool = is_async  # 是否同步快照
        self.name: str = ""

    def serialize(self) -> dict:
        d = self.__dict__
        d["name"] = d.__class__.__name__[:-9].lower()
        return d

