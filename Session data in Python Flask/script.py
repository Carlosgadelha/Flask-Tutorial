from flask import Flask, session, redirect, url_for, escape, request 
app = Flask(__name__) 
app.secret_key = 'qualquer string aleatória'

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index'))
   return '''
	
   <form action = "" method = "post">
      <p><input type = text name = username/></p>
      <p<<input type = submit value = Login/></p>
   </form>	
'''

# The application also contains a logout () view function that pops up the 'username' session variable.Therefore, the ' /' URL displays the start page again.

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))