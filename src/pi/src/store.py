#!/usr/bin/python3

import json
import time
import datetime
dt = datetime.datetime.now()
from readSensors import readSensors as read

path='/home/pi/fyp/jsonData/'
end='.json'

#Change this to store as json
def store(data):
    fileName=str(dt.strftime("%Y%d%m%H"))
    timeStamp = str(dt.strftime("%Y/%m/%d %H:%M:%S"))
    entry={timeStamp:data}
    with open(path+fileName+end, 'a') as file:
        json.dump(entry, file,indent=2)
    return

def pushToDatabase(data):
    pass

if __name__ == '__main__':
    tt=time.time()
    values = read()
    store(values)

    print('fin')
    print('total time taken:',time.time()-tt)
