

class Component(object):

    def __init__(self, is_async: bool = True):
        self.is_async: bool = is_async  # 是否同步快照

    def serialize(self) -> dict:
        d = {}
        d["name"] = d.__class__.__name__[:-9].lower()
        for k, v in self.__dict__.items():
            if isinstance(v, object):
                v = v.__dict__
            d[k] = v
        return d

