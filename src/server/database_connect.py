import mysql.connector 
from mysql.connector import Error
import os
from datetime import datetime 

file = open('sample_sensor_values.txt', 'r')
def collect(val): 
	
	x = mysql.connector.connect( 
	user=os.environ['db_username'], 
	host=os.environ['db_host'], 
	passwd=os.environ['db_password'], 
	database='mydb'
	)

	mycursor = x.cursor()

	value = []
	
	for line in file.readlines(): 
		line = line.split(" ") 
		dts = (line[0] + " " + line[1])
		value.append(str(dts))
		print(value)
	
	for item in value: 
		sql = ("""INSERT INTO sensor_val (timer) VALUES ('{}') """).format(item)

	# dtspushable = datetime.strptime(dts, '%Y-%m-%d %H:%M:%S')
	# testpushable = dtspushable.strftime('%Y-%m-%d %H:%M:%S')
	
	# print(type(testpushable))
		
		mycursor.execute(sql)
			
		x.commit()
		print(mycursor.rowcount, "record inserted")

	x.close()
	file.close()

collect(file)
