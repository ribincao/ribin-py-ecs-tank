import signal
from typing import Tuple


def signal_handler():
    import warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    def receive_signal(signum, stack):
        exit(-1)
    signal.signal(signal.SIGQUIT, receive_signal)
    signal.signal(signal.SIGINT, receive_signal)
    signal.signal(signal.SIGTERM, receive_signal)
    signal.signal(signal.SIGABRT, receive_signal)
    signal.signal(signal.SIGSEGV, receive_signal)


class Vector2(object):

    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    @staticmethod
    def zero():
        return Vector2(0.0, 0.0)

    def to_tuple(self) -> Tuple[float, float]:
        return self.x, self.y

