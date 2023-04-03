from common.logger import logger
from typing import Tuple


class Buffer(object):
    """
    |matrix|xxxx|<-------->
    """
    FRAME_HEADER_LENGTH = 10
    FRAME_LIMIT = 1 << 20
    FRAME_MAGIC = b'MATRIX'

    def __init__(self):
        super(Buffer, self).__init__()
        self._offset: int = 0
        self._buffer: bytes = b''

    def receive_data(self, data: bytes) -> bytes:
        receive_data = self._buffer + data
        length, data = self.try_get_packet(receive_data, self._offset)
        if length + self.FRAME_HEADER_LENGTH == len(data):
            self._buffer = receive_data[len(data):]
            return data

        self._buffer = data
        return b""

    def try_get_packet(self, data: bytes, start_pos: int) -> Tuple[int, bytes]:
        if not data:
            logger.warning(f"client closed.")
            return 0, b''
        size = len(data)

        if size > self.FRAME_LIMIT:
            logger.error(f"Frame is too long {data}")
            return 0, b''

        if start_pos < 0 or start_pos >= size:
            return 0, b''

        if size < start_pos + self.FRAME_HEADER_LENGTH:
            return 0, data[start_pos:]

        header = data[:self.FRAME_HEADER_LENGTH]
        magic = header[:6]
        if magic != self.FRAME_MAGIC:
            logger.error(f"invalid packet start")
            return 0, b''
        length = int.from_bytes(header[6:], "little")

        if size < start_pos + length + self.FRAME_HEADER_LENGTH:
            return length, data[start_pos:]

        return length, data[start_pos:start_pos + length + self.FRAME_HEADER_LENGTH]


