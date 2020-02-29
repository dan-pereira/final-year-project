from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route('/login/<user1r>')
def login(user): 
	user1 = {'username' : user}
	return render_template('login.html', title = 'Login', user = user1)

@app.route('/home')
def homescreen():
	return render_template('index.html', title = 'Home')

@app.route('/graphs')
def graph():#graph_type):
	return render_template('graphs.html', title = 'Graphs' ''', var = var''')

app.route('/dash')
def dash():
	return render_template('dashboard.html', title = 'Dashboard' ''', var = var''')

@app.errorhandler(404)
def invalidroute(e): 
	return ('Sorry! Please check your URL and try again')

if __name__ == '__main__': 
	app.run(host = '127.0.0.1', port = 80, debug = True)	 #,ssl_context = ('cert.pem', 'key.pem'))
