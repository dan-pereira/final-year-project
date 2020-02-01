from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route('/login/<user>')
def login(user): 
	user1 = {'username' : user}
	return render_template('index.html', title = 'Home', user = user1)

@app.route('/graphs')
def graph(graph_type):
	return('graph')

if __name__ == '__main__': 
	app.run(host = '0.0.0.0', port = 80)