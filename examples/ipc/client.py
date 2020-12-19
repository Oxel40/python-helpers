import helpers.ipc
import time
import numpy as np


address = ('localhost', 6000)

# time.sleep(3)
for _ in range(10000):
    ans = ipc.remote_call(address, "test", "ett", "2", 3)
    print(ans)

    arr = np.random.rand(3, 2)
    ans = ipc.remote_call(address, "arrmax", arr)
    print(arr, ans, sep='\n')
