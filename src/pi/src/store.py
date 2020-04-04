#!/usr/bin/python3

import os.path
import os
import json
import time
import datetime
dt = datetime.datetime.now()
from readSensors import readSensors as read

path='/home/pi/fyp/data/'
end='.json'

#Change this to store as json
def store(data):
    fileName=str(dt.strftime("%Y%m%d%H"))
    timeStamp = str(dt.strftime("%Y/%m/%d %H:%M:"))+"00"
    entry={timeStamp:data}
    fileName=path+fileName+end

    if not os.path.isfile(fileName):
        print('not there')
        with open(fileName, 'a') as file:
            empty={}
            json.dump(empty, file,indent=2)

    with open(fileName, "r+") as file:
        print('write')
        data = json.load(file)
        data.update(entry)
        file.seek(0)
        json.dump(data, file,indent=2)
    return

def pushToDatabase(data):
    pass

if __name__ == '__main__':
    tt=time.time()
    values = read()
    store(values)

    print('fin')
    print('total time taken:',time.time()-tt)
