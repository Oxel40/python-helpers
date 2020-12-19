from helpers.loading_bar import SimpleLoadingBar
import time


bar = SimpleLoadingBar()

bar.start(msg='Starting...')
for x in range(100):
    time.sleep(0.1)
    bar.set(x/100, msg=f'x is {x}...')

bar.finish(msg='Done!')
