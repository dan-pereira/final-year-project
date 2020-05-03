import mysql.connector
from mysql.connector import Error
import os
from datetime import datetime

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
    #print(result)
    x.close()
    return result

if __name__ == "__main__":
    result = queryDB('SELECT moisture1,moisture2, moisture3 FROM mydb.sensor_val order by timer desc limit 3')

    result = queryDB('SELECT timer, moisture1 FROM mydb.sensor_val order by timer desc limit 5')

    value = []
    for item in result:
        # print(item)
        value.append(item)
    stamplist = []
    stamplist = [x[0] for x in value]
    moisturelist = [x[1] for x in value]
    stamp = []
    moist  = []
    for x in stamplist:
        stamp.append(x.strftime('%Y-%m-%d %H:%M:%S'))

    for x in moisturelist:
        moist.append(x)

    print(moisturelist)

