from net.buffer import Buffer


class Codec(object):

    def __init__(self):
        pass

    def decode(self, data: bytes) -> str:
        _ = self
        s = data[Buffer.FRAME_HEADER_LENGTH:].decode()
        return s

    def encode(self, data: str) -> bytes:
        _ = self
        b = data.encode()
        length = len(b).to_bytes(4, "little")
        return Buffer.FRAME_MAGIC + length + b
