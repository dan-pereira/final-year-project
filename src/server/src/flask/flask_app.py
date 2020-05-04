#!/usr/bin/python3
import sys
from flask import Flask, render_template, redirect
import boto3 
import os
sys.path.append('../')
from database_query import *
from manualWater import waterPlant

app = Flask(__name__)

@app.route('/login/<user>')
def login(user): 
	user1 = {'username' : user}
	return render_template('login.html', title = 'Login', user = user)

@app.route('/home')
def homescreen():
	return render_template('index.html', title = 'Home')

@app.route('/graphs')
def graph():#graph_type)
	result = query('SELECT timer, moisture1 FROM mydb.sensor_val order by timer desc limit 5')
	result1 = query('SELECT timer, moisture2 FROM mydb.sensor_val order by timer desc limit 5')
	result2 = query('SELECT timer, moisture3 FROM mydb.sensor_val order by timer desc limit 5')
	label = result[0]
	value = result[1]
	vals2 = result1[1]
	vals3 = result2[1] 
	return render_template('graphs.html', title = 'Graphs' ''', var = var''',labels1 = label, values1 = value, values2 = vals2, values3 = vals3)

app.route('/dash')
def dash():
	return render_template('dashboard.html', title = 'Dashboard' ''', var = var''')

@app.route('/water/<plant_number>')
def water(plant_number):
	response = waterPlant(plant_number)
	print('watered')
	return redirect('/graphs')

@app.errorhandler(404)
def invalidroute(e): 
	return ('Sorry! Please check your URL and try again')

if __name__ == '__main__': 
	app.run(host = '127.0.0.1', port = 5000, debug = True)
	