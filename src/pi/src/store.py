#!/usr/bin/python3
import os.path
import os
import sys
import json
import time
import datetime
import mysql.connector
from mysql.connector import Error
from readSensors import readSensors as read

dt = datetime.datetime.now()

path = '/home/pi/src/data/'
end = '.json'


def storeLocal(entry):
    fileName = str(dt.strftime("%Y%m%d%H"))
    fileName = path + fileName + end

    if not os.path.isfile(fileName):
        print('not there')
        with open(fileName, 'a') as file:
            empty = {}
            json.dump(empty, file, indent=2)

    with open(fileName, "r+") as file:
        print('write')
        data = json.load(file)
        data.update(entry)
        file.seek(0)
        json.dump(data, file, indent=2)
    return


def send(json_vals):
    print('send')

    x = mysql.connector.connect(
        user=os.environ['db_username'],
        host=os.environ['db_host'],
        passwd=os.environ['db_password'],
        database='mydb'
    )
    mycursor = x.cursor()

    for ts in json_vals:
        sensor_bank = []
        timestamp = json_vals.get(ts)

        sensor_bank.append(ts)
        sensors = ['mcp00', 'mcp01', 'mcp02', 'mcp07', 'soilTemp', 'airTemp', 'humidity']
        for sensor in sensors:
            sensor_bank.append(timestamp.get(sensor))

        sql = (
            """INSERT INTO sensor_val (timer, moisture1, moisture2, moisture3, water_level, soiltemp1, air_temp, air_humid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s ) """)

        tuple1 = (
        sensor_bank[0], sensor_bank[1], sensor_bank[2], sensor_bank[3], sensor_bank[4], sensor_bank[5], sensor_bank[6],
        sensor_bank[7])

        mycursor.execute(sql, tuple1)
        x.commit()

    x.close()
    return


def scoop():
    '''iterate files in path remove if recieved'''

    files = os.listdir(path)

    print(files)
    for fileName in files:
        if fileName[-5:] == '.json':
            fileName = path + fileName
            with open(fileName, 'r') as json_file:
                data = json_file.read()
            print(fileName)
            json_vals = json.loads(data)

            try:
                print('Found Unbacked Up Files')
                send(json_vals)
                print('scoop sent')
                os.remove(fileName)
                print(fileName)
            except:
                print('scoop no send')
    return


if __name__ == '__main__':
    tt = time.time()

    try:
        values = read()
    except:
        print('Read program failed')
        sys.exit('Read program failed')

    timeStamp = str(dt.strftime("%Y-%m-%d %H:%M:")) + "00"
    entry = {timeStamp: values}

    try:
        send(entry)

    except:
        storeLocal(entry)
        print("couldnt connect")

    scoop()

    print('total time taken:', time.time() - tt)
    sys.exit()
