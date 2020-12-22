import helpers.ipc as ipc
import numpy as np
from enum import Enum


class en(Enum):
    A = 1
    B = 2
    C = 3


address = ('localhost', 6000)
router = ipc.Router(address, authkey=b'test')


@router.expose
def test(one, two, three):
    return (three, two, one)


@router.expose
def arrmax(arr: np.ndarray):
    return arr.max()


@router.expose
def enBTest(enu):
    return [x == enu.B for x in en]


router.serve()
