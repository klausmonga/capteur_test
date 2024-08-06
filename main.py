import time
import os
import json
import random
import multiprocessing
import time

def Onstart():
    b = 0
    while 1:
        # print(b)
        time.sleep(1)
        random.random()
        b = random.randint(0, 50)
        os.system("/usr/bin/mosquitto_pub -h 127.0.0.1 -t ch1/temp -m V9:" + str(b))

