#!/usr/bin/python3
'''
will start on boot via systemd
systemctl status flask-app
sudo systemctl restart flask-app
'''
import sys
sys.path.append("/home/pi/src/")
#import controllers
from flask import Flask
from flask import render_template
from flask import request
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/pi/src/configs'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/update_config', methods=['POST'])
def updateconfig():
    #return('hello world')
    file = request.files['file']
    #files = {'file': ('test.txt': open('test.txt', 'rb'))}
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return 'file uploaded'

@app.route('/water_plant', methods=['POST'])
def water():
    plantNo = request.form
    return str(plantNo)

if __name__ == '__main__':
         app.run(host = 'localhost', port = '5000', debug = True) #,ssl_context = ('cert.pem', 'key.pem'))
