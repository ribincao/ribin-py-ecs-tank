from typing import Callable, Dict, List


class IEvent(object):

    def __init__(self):
        pass


class EntityCreateEvent(IEvent):

    def __init__(self, uid: int):
        super(EntityCreateEvent, self).__init__()
        self.uid: int = uid


class EntityDestroyEvent(IEvent):

    def __init__(self, uid: int):
        super(EntityDestroyEvent, self).__init__()
        self.uid: int = uid


class EventDispatch(object):

    def __init__(self):
        self._handlers: Dict[str, List[Callable]] = {}

    def register_event(self, event_name: str, func: Callable):
        if event_name not in self._handlers:
            self._handlers[event_name] = []
        self._handlers[event_name].append(func)

    def dispatch_event(self, event: IEvent):
        event_name = event.__class__.__name__
        if event_name not in self._handlers:
            return
        try:
            for handler in self._handlers[event_name]:
                handler(event)
        except Exception as error:
            print(f"{event_name} exec error: {error}")


if __name__ == '__main__':
    class ITest(EventDispatch):

        def __init__(self):
            super(ITest, self).__init__()

    class Test(ITest):

        def __init__(self):
            super(Test, self).__init__()
            self.register_event("EntityCreateEvent", self.hello)

        def hello(self, event: EntityCreateEvent):
            print(f"hello, {event.uid}")

    t = Test()
    e = EntityCreateEvent(1)
    t.dispatch_event(e)
