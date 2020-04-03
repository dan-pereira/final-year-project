import mysql.connector 
from mysql.connector import Error
import os
from datetime import datetime 

def query(): 
	
	x = mysql.connector.connect( 
	user=os.environ['db_username'], 
	host=os.environ['db_host'], 
	passwd=os.environ['db_password'], 
	database='mydb'
	)

	mycursor = x.cursor()

	mycursor.execute("SELECT * FROM sensor_val") 

	result = mycursor.fetchall() 
	# print(result)

	x.close() 

	value = []
	for item in result: 
		# print(item)
		value.append(item) 

	# print(value)

	stamplist = []
	stamplist = [x[0] for x in value]
	stamp = []
	
	for x in stamplist: 
		stamp.append(x.strftime('%Y-%m-%d %H:%M:%S'))

	# print(stamp)
	return stamp
query()
