import helpers.ipc as ipc
import numpy as np
from enum import Enum


class en(Enum):
    A = 1
    B = 2
    C = 3


address = ('localhost', 6000)
remote = ipc.Remote(address, authkey=b'test')


ans = remote.remote_call('test', 'ett', '2', 3)
print(ans)

arr = np.random.rand(3, 2)
ans = remote.remote_call('arrmax', arr)
print(arr, ans, sep='\n')

print(remote.remote_call('enBTest', en.B))
