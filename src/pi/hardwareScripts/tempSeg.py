#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from datetime import datetime

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import viewport, sevensegment

import os
import glob
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        line = read_temp_raw()
    ep = lines[1].find('t=')
    if ep != -1:
        ts = lines[1][ep+2:]
        tc = float(ts) / 1000.0
        return tc

def main():
    # create seven segment device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1)
    seg = sevensegment(device)

    #update temp every second
    print('Take Temps')
    while True:
        reet = str(read_temp())[:5]
        if len(reet) < 5:
            reet += "0"
        seg.text = reet+'.C'
        time.sleep(1.0)


if __name__ == '__main__':
    main()
