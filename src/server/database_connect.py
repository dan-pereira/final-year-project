import mysql.connector 
from mysql.connector import Error
import os
from datetime import datetime 
import json

def collect(): 
	with open('sample_sensor_values.json', 'r') as json_file: 
		data = json_file.read() 

	json_vals = json.loads(data)
	
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
		for sensor_name in timestamp: 
			if sensor_name in ('mcp00', 'mcp01', 'mcp02', 'mcp07', 'soilTemp', 'airTemp', 'humidity'):
				sensor_bank.append(timestamp.get(sensor_name))
		# print(sensor_bank[1])
		sql = ("""INSERT INTO sensor_val (timer, moisture1, moisture2, moisture3, water_level, soiltemp1, air_temp, air_humid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s ) """)
		
		tuple1 = (sensor_bank[0], sensor_bank[1], sensor_bank[2], sensor_bank[3], sensor_bank[4], sensor_bank[5], sensor_bank[6], sensor_bank[7])
		
		mycursor.execute(sql, tuple1)
		x.commit()
		# print(mycursor.rowcount, "record inserted")

	x.close()

collect()
