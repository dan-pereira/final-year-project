#!/usr/bin/python3
import mysql.connector
import os


def queryDB(query):
    x = mysql.connector.connect(
        user=os.environ['db_username'],
        host=os.environ['db_host'],
        passwd=os.environ['db_password'],
        database='mydb'
    )

    mycursor = x.cursor()
    mycursor.execute(query)
    result = mycursor.fetchall()

    x.close()
    return result


def formattedQDB(query):
    result = queryDB(query)

    value = []
    for item in result:
        value.append(item)

    stamplist = []
    stamplist = [x[0] for x in value]
    moisturelist = [x[1] for x in value]
    stamp = []
    moist = []
    for x in stamplist:
        stamp.append(x.strftime('%Y-%m-%d %H:%M:%S'))

    for x in moisturelist:
        moist.append(x)

    print(stamp)
    print(moisturelist)

    return (stamp, moisturelist)


if __name__ == "__main__":
    value = queryDB(
        'SELECT moisture1,moisture2, moisture3, air_temp,air_humid FROM mydb.sensor_val order by     timer desc limit 5')
    print(value)
    value = formattedQDB('SELECT timer, moisture1 FROM mydb.sensor_val order by timer desc limit 5')
    print(value)
