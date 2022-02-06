from flask import Flask
from flask import render_template
# import flask as Flask
app = Flask (__name__)

@app.route('/enternew')
def new_student():
   return render_template('student.html')