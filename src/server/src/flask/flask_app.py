#!/usr/bin/python3
import sys
from flask import Flask, render_template, redirect

sys.path.append('./')
from database_query import formattedQDB
from manualWater import waterPlant, manAutoSelect, readConfig

app = Flask(__name__)


@app.route('/login/<user>')
def login(user):
    user1 = {'username': user}
    return render_template('login.html', title='Login', user=user)


@app.route('/home')
def homescreen():
    return render_template('index.html', title='Home')


@app.route('/graphs', methods=['GET', 'POST'])
def graph():  # graph_type)
    result = formattedQDB('SELECT timer, moisture1 FROM mydb.sensor_val order by timer desc limit 5')
    result1 = formattedQDB('SELECT timer, moisture2 FROM mydb.sensor_val order by timer desc limit 5')
    result2 = formattedQDB('SELECT timer, moisture3 FROM mydb.sensor_val order by timer desc limit 5')
    waterlev1 = formattedQDB('SELECT timer, water_level FROM mydb.sensor_val order by timer desc limit 5')
    airtemp1 = formattedQDB('SELECT timer, air_temp FROM mydb.sensor_val order by timer desc limit 5')
    airhumid1 = formattedQDB('SELECT timer, air_humid FROM mydb.sensor_val order by timer desc limit 5')
    label = result[0]
    value = result[1]
    vals2 = result1[1]
    vals3 = result2[1]
    waterlev = waterlev1[1]
    air = airtemp1[1]
    airhumid = airhumid1[1]
    statey = readConfig()
    for k, v in statey.items():
        if k == 'manual_mode':
            mode_status = v

    if mode_status == 0:
        state = 'automatic'
    else:
        state = 'manual'

    return render_template('graphs.html', title='Graphs' ''', var = var''', labels1=label, values1=value, values2=vals2,
                           values3=vals3, waterlevel=waterlev, airtemperature=air, airhumidity=airhumid,
                           modestate=state)


app.route('/dash')


def dash():
    return render_template('dashboard.html', title='Dashboard' ''', var = var''')


@app.route('/water/<int:plant_number>')
def water(plant_number):
    print('----++', plant_number)
    response = waterPlant(plant_number)
    print(response)
    return redirect('/graphs')


@app.route('/mode/<int:val>')
def modeselect(val):
    manAutoSelect(val)
    print('mode ', val, ' selected')
    return redirect('/graphs')


@app.errorhandler(404)
def invalidroute(e):
    return ('Sorry! Please check your URL and try again')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
