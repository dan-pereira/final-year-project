from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route('/<user>')
def test(user): 
	user1 = {'username' : user}
	return render_template('index.html', title = 'Home', user = user1)

if __name__ == '__main__': 
	app.run(host = '0.0.0.0', port = 80)