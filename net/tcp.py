import asyncio
from typing import Optional
from net.connection import Connection
from common.logger import logger
from logic.context import Context


class Tcp(object):

    def __init__(self, port: int, name: str, context: Context):
        self._port: int = port
        self._name: str = name
        self._context: Context = context
        self._is_client: bool = False
        self._client_connection: Optional[Connection] = None

    async def run_server(self):
        async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
            connection = Connection(reader, writer, self._context)

            logger.info(f"client connected.")
            await connection.handle_message()

        server = await asyncio.start_server(handle_client, port=self._port)
        logger.info(f"{self._name} Server started on {server.sockets[0].getsockname()}")
        async with server:
            await server.serve_forever()

    async def run_client(self, host: str, port: int):
        reader, writer = await asyncio.open_connection(host, port)
        connection = Connection(reader, writer, self._context)
        self._is_client = True
        self._client_connection = connection
        await self._client_connection.connect()
    
    @property
    def connection(self) -> Optional[Connection]:
        if not self._is_client:
            return None
        return self._client_connection
