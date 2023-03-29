import asyncio
from typing import Optional
from common.logger import logger
from net.buffer import Buffer
from net.codec import Codec
from logic.context import Context


class Connection(object):

    def __init__(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter, context: Context):
        super(Connection, self).__init__()
        self.reader: asyncio.StreamReader = reader
        self.writer: asyncio.StreamWriter = writer
        self.buffer: Buffer = Buffer()
        self.codec: Codec = Codec()
        self.context: Context = context

    def close(self):
        self.writer.close()
        self._is_close = True

    async def handle_message(self):
        try:
            while not self._is_close:
                data = await self.receive_message()
                if not data:
                    break
                message = self.codec.decode(data)
                logger.info(f"server receive_message {message}")
            self.close()
        except Exception as error:
            self.close()

    async def receive_message(self) -> Optional[bytes]:
        while not self._is_close:
            data = await self.reader.read(1024)
            if not data:
                return data
            message = self.buffer.receive_data(data)
            if not message:
                continue
            return message

    async def send_message(self, message: str):
        data = self.codec.encode(message)
        self.writer.write(data)
        await self.writer.drain()

    async def connect(self):
        while not self._is_close:
            try:
                data = await self.receive_message()
                if not data:
                    self.close()
                    break
                message = self.codec.decode(data)
                logger.info(f"client receive_message {message}")
            except Exception as e:
                logger.error(f"Error: {e}")
                self.close()
            await asyncio.sleep(3)

