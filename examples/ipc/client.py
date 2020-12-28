import helpers.ipc as ipc
import numpy as np
from enum import Enum


class en(Enum):
    A = 1
    B = 2
    C = 3


address = ('localhost', 6000)
remote = ipc.Remote(address, authkey=b'test')


ans = remote.call('test', 'ett', '2', 3)
print(ans)

arr = np.random.rand(3, 2)
ans = remote.call('arrmax', arr)
print(arr, ans, sep='\n')

print(remote.call('enBTest', en.B))

# Test KeyError
try:
    remote.call('notAFunction')
except KeyError as e:
    print('A KeyError occured:', e)
