from multiprocessing.connection import Listener, Client
from multiprocessing.context import AuthenticationError
import socket


class Router:
    def __init__(self, address, authkey=b'super secret'):
        self.address = address
        self.authkey = authkey

        self.func_map = dict()

    def expose(self, func):
        if func.__name__ in self.func_map.keys():
            raise Exception(
                f'{func.__name__} already exists as an exposed function in this {self.__name__}')
        self.func_map[func.__name__] = func

        return func

    def call(self, func_name, *args, **kwargs):
        return self.func_map[func_name](*args, **kwargs)

    def serve(self):
        with Listener(self.address, authkey=self.authkey) as listener:
            # Set timeout to allow keyboard interupts
            listener._listener._socket.settimeout(3)
            while True:
                try:
                    conn = listener.accept()
                    print('\nconnection accepted from', listener.last_accepted)
                    func_name, args, kwargs = conn.recv()
                    print(func_name, args, kwargs)
                    conn.send(self.call(func_name, *args, **kwargs))
                    conn.close()
                except socket.timeout:
                    print('timeout reached...')
                except AuthenticationError as e:
                    print('(!) Authentication failed')
                    print(e)
                except (ConnectionResetError, ConnectionAbortedError, EOFError) as e:
                    print('(!) Something bad happened with the connection')
                    print(e)


class Remote:
    def __init__(self, address, authkey=b'super secret'):
        self.address = address
        self.authkey = authkey

    def remote_call(self, func_name, *args, **kwargs):
        conn = Client(self.address, authkey=self.authkey)
        conn.send((func_name, args, kwargs))
        res = conn.recv()
        conn.close()
        return res
