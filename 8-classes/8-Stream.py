# Inheriting from base Exception Class
class InvalidOPerationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOPerationError("Stream is  already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOPerationError("Stream is  already closed")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print('Reading from a file')


class NetworkStream(Stream):
    def read(self):
        print('Reading from a network stream')
