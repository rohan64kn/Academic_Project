# app.py

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

# Set a secret key for encrypting session data
app.secret_key = 'my_secret_key'

# dictionary to store user and password
users = {
	'shubh':['007','Admin'],
	'rohit' :['008','influencers'],
	'bala' : ['009','sponsors']
}
# To render a login form 
@app.route('/')
def view_form():
	return render_template('login.html')
# For handling post request form we can get the form
# inputs value by using POST attribute.
# this values after submitting you will never see in the urls.
@app.route('/handle_post', methods=['POST'])
def handle_post():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if username in  users:
			lst =  users[username]
			if lst[0] == password:
				if lst[1] == 'Admin':
					return render_template('home_admin.html')
				if lst[1] == 'influencers':
					return render_template('home_influ.html')
				if lst[1] == 'sponsors':
					return render_template('home_spon.html')
			else:   
				return '<h1>Invalid credentials!</h1>'
		else:   
			return '<h1>Invalid credentials!</h1>'
	else:   
		return render_template('login.html')

if __name__ == '__main__':
	app.run(debug=True, port=1443)


  
