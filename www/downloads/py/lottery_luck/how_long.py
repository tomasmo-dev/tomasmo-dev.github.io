import random
import time
from numba import jit

target = [1, 2, 3, 4, 5]
rList = []

i = 0

RUNNING = True

startTime = time.time()
@jit
def run(TARGETCON, num, RUNLOOP):

    while RUNLOOP:

        for i in range(0, 5):
            rNum = random.randint(1, 49)
            rList.append(rNum)
            #print(rNum, "\n")
        if rList == TARGETCON:
            RUNLOOP = False
            endtime = time.time()
            EndDate = time.localtime(time.time())
            print(rList, target, num, endtime - startTime, startTime, endtime, EndDate, sep='|')
        else:
            print(rList)
            rList.clear()
            num = num + 1

run(target, i, RUNNING)

