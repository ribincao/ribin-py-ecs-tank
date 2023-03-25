
from common.singleton import Singleton
import asyncio
import time


class Timer(Singleton):
    LOGIC_RATE = 100e-3

    def __init__(self):
        self._start_tick = self.get_current_ms()
        self._tick_count: int = 0

    async def update(self):
        while True:
            self._tick_count += 1
            await asyncio.sleep(self.LOGIC_RATE)

    def get_current_tick(self):
        return self._tick_count

    @staticmethod
    def get_current_ms():
        return int(round(time.time() * 1000))

    def second_to_tick(self, second: int) -> int:
        return int(second / self.LOGIC_RATE)


timer = Timer()

