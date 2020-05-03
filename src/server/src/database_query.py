import mysql.connector 
from mysql.connector import Error
import os
from datetime import datetime 

def query(query): 
    
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

    print(result)

    value = []
    for item in result: 
        # print(type(item))
        value.append(item) 

    # print(value)

    stamplist = []
    stamplist = [x[0] for x in value]
    moisturelist = [x[1] for x in value]
    stamp = []
    moist  = []
    for x in stamplist: 
        stamp.append(x.strftime('%Y-%m-%d %H:%M:%S'))

    for x in moisturelist: 
        moist.append(x)

    print(stamp)
    print(moisturelist)

    return (stamp, moisturelist)
if __name__ == "__main__":
    result = (query('SELECT timer, moisture1 FROM mydb.sensor_val order by timer desc limit 1'))

#     # print(result)
#     i = 0
#     while i<len(result[0]): 
#         listy.append(result[0][i])
#         listy.append(result[1][i])
#         # print(result[1][i])

#         i += 1

#     for item in listy: 
#         print(str(item))