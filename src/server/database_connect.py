import mysql.connector 
import os
# print(os.environ['db_username'])

# try:
x = mysql.connector.connect( 
	user=os.environ['db_username'], 
	host=os.environ['db_host'], 
	password=os.environ['db_password'], 
	database='mydb'
)

# except mysql.connector.Error as err: 
# 	print(err)

# # else:
# 	x.close()

mycursor = x.cursor()

sql = "INSERT INTO sensor_values (moisture_value, temperature) VALUES (2, 11)"
# val = (12)

mycursor.execute(sql) 

x.commit() 

print(mycursor.rowcount, "record inserted")
x.close()