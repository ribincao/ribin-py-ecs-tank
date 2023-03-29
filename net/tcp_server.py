import asyncio
from typing import Optional
from net.connection import Connection
from common.logger import logger


class Tcp(object):

    def __init__(self, port: int, name: str):
        self._port: int = port
        self._name: str = name
        self._is_client: bool = False
        self._client_connection: Optional[Connection] = None

    async def run_server(self):
        async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
            connection = Connection(reader, writer)

            logger.info(f"client connected.")
            await connection.handle_message()

        server = await asyncio.start_server(handle_client, port=self._port)
        logger.info(f"{self._name} Server started on {server.sockets[0].getsockname()}")
        async with server:
            await server.serve_forever()

    async def run_client(self, host: str, port: int):
        reader, writer = await asyncio.open_connection(host, port)
        connection = Connection(reader, writer)
        self._is_client = True
        self._client_connection = connection
        await self._client_connection.connect()
