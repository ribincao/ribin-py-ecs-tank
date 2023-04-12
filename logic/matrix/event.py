from typing import Callable, List


class Event(object):

    def __init__(self):
        self._handlers: List[Callable] = []

    def __call__(self, *args, **kwargs):
        for handler in self._handlers:
            handler(*args, **kwargs)

    def __add__(self, handler: Callable) -> 'Event':
        if handler not in self._handlers:
            self._handlers.append(handler)
        return self

    def __sub__(self, handler: Callable) -> 'Event':
        if handler in self._handlers:
            self._handlers.remove(handler)
        return self



