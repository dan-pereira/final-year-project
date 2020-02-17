from flask import Flask 

app = Flask(__name__)

@app.route('/home')
def homescreen():
	return ('Hello World!')

if __name__ == '__main__': 
	app.run(host = '0.0.0.0', port = 80)	 #,ssl_context = ('cert.pem', 'key.pem'))
