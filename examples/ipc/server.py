import helpers.ipc
import numpy as np

router = ipc.Router()


@router.expose
def test(one, two, three):
    print(three, two, one)
    return (three, two, one)


@router.expose
def arrmax(arr: np.ndarray):
    print(arr.max())
    return arr.max()


address = ('localhost', 6000)
router.serve(address)
