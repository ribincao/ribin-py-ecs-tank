import asyncio
from typing import Optional
from common.logger import logger
from net.buffer import Buffer
from net.codec import Codec
from logic.context import Context
from logic.manager.command_manager import command_manager
import time


class Connection(object):
    SNAP_RATE = 66e-100
    NET_RATE = 20e-100

    def __init__(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter, context: Context):
        super(Connection, self).__init__()
        self.reader: asyncio.StreamReader = reader
        self.writer: asyncio.StreamWriter = writer
        self.buffer: Buffer = Buffer()
        self.codec: Codec = Codec()
        self.context: Context = context
        self._is_close: bool = False
        self.last_world: str = ""
        self.uid: int = -1
        self.last_active_time: int = 0

    def update_active_time(self):
        self.last_active_time = int(time.time())

    def close(self):
        self.writer.close()
        self._is_close = True
        self.context.destroy_entity(self.uid)
        logger.debug(f"{self.uid} close connection.")

    async def handle_message(self):
        try:
            while not self._is_close:
                data = await self.receive_message()
                if not data:
                    break
                message = self.codec.decode(data)
                cmd = command_manager.create_cmd(message)
                logger.debug(f"server receive_cmd {cmd.__dict__}")
                if cmd:
                    self.context.input_command(cmd)
                    self.uid = cmd.uid
                    self.update_active_time()
            self.close()
        except Exception as error:
            logger.error(f"handle_message_error: {error}")
            self.close()

    async def export_world(self):
        try:
            while not self._is_close:
                world = self.context.export_world()
                if world != self.last_world:
                    logger.debug(f"server export world {world}.")
                    self.last_world = world
                    await self.send_message(world)
                await asyncio.sleep(self.SNAP_RATE)
            self.close()
        except Exception as error:
            logger.error(f"export_world_error: {error}")
            self.close()

    async def import_world(self):
        try:
            while not self._is_close:
                data = await self.receive_message()
                if not data:
                    break
                message = self.codec.decode(data)
                logger.debug(f"client import world {message}.")
                self.context.import_world(message)
                if not self.context.is_connected:
                    self.context.is_connected = True
                
                self.update_active_time()
            self.close()
        except Exception as error:
            logger.error(f"import_world_error: {error}")
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
        # await self.writer.drain()

    async def connect(self):
        while not self._is_close:
            try:
                messages = self.context.messages
                self.context.messages = []
                for command in messages:
                    message = command.encode() 
                    logger.info(f"client send_command {message}")
                    await self.send_message(message)
            except Exception as e:
                logger.error(f"connect_error: {e}")
                self.close()
            await asyncio.sleep(self.NET_RATE)

