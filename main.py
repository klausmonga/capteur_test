import time
import os
import json
import random
import multiprocessing
import time

def Onstart(extra_bundel):
    b = 0
    pr1_trigger = extra_bundel['remote_params']['pr1_trigger']
    pr2_trigger = extra_bundel['remote_params']['pr2_trigger']
    pr3_trigger = extra_bundel['remote_params']['pr3_trigger']
    os.system("/usr/bin/mosquitto_pub -h 127.0.0.1 -t ch1/power -m 1")
    while 1:
        # print(b)
        time.sleep(7)
        random.random()
        pr1 = random.randint(0, 10)
        pr2 = random.randint(0, 10)
        pr3 = random.randint(0, 10)
        temp1 = random.randint(0, 100)
        temp2 = random.randint(0, 100)
        temp3 = random.randint(0, 100)
        os.system("/usr/bin/mosquitto_pub -h 127.0.0.1 -t ch1/temp -m " + str(temp1))
        os.system("/usr/bin/mosquitto_pub -h 127.0.0.1 -t ch2/temp -m " + str(temp2))
        os.system("/usr/bin/mosquitto_pub -h 127.0.0.1 -t ch3/temp -m " + str(temp3))
        os.system("/usr/bin/mosquitto_pub -h 127.0.0.1 -t ch1/pression -m " + str(pr1))
        os.system("/usr/bin/mosquitto_pub -h 127.0.0.1 -t ch2/pression -m " + str(pr2))
        os.system("/usr/bin/mosquitto_pub -h 127.0.0.1 -t ch3/pression -m " + str(pr3))
        if pr1 > pr1_trigger:
            os.system("/usr/bin/mosquitto_pub -h 127.0.0.1 -t ch1/power -m 0")
        else:
            os.system("/usr/bin/mosquitto_pub -h 127.0.0.1 -t ch1/power -m 1")

        if pr2 > pr2_trigger:
            os.system("/usr/bin/mosquitto_pub -h 127.0.0.1 -t ch2/power -m 0")
        else:
            os.system("/usr/bin/mosquitto_pub -h 127.0.0.1 -t ch2/power -m 1")

        if pr3 > pr3_trigger:
            os.system("/usr/bin/mosquitto_pub -h 127.0.0.1 -t ch3/power -m 0")
        else:
            os.system("/usr/bin/mosquitto_pub -h 127.0.0.1 -t ch3/power -m 1")