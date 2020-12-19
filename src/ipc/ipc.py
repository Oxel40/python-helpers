from multiprocessing.connection import Listener, Client
import socket


class Router:
    def __init__(self) -> None:
        self.func_map = dict()

    def expose(self, func):
        if func.__name__ in self.func_map.keys():
            raise Exception(
                f'{func.__name__} already exists as an exposed function in this {self.__name__}')
        self.func_map[func.__name__] = func

        return func

    def call(self, func_name, *args, **kwargs):
        return self.func_map[func_name](*args, **kwargs)

    def serve(self, address, authkey=b'super secret'):
        with Listener(address, authkey=authkey) as listener:
            listener._listener._socket.settimeout(3)
            while True:
                try:
                    conn = listener.accept()
                except socket.timeout as t:
                    print('to')
                    continue
                print('connection accepted from', listener.last_accepted)
                func_name, args, kwargs = conn.recv()
                print(func_name, args, kwargs)
                conn.send(self.call(func_name, *args, **kwargs))
                conn.close()


def remote_call(address, func_name, *args, **kwargs):
    conn = Client(address, authkey=b'super secret')
    conn.send((func_name, args, kwargs))
    res = conn.recv()
    conn.close()
    return res
