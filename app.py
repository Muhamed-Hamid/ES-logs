#!/usr/bin/python
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
import json
from wtforms import Form, StringField, TextAreaField, validators
from search import search

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/smpp')
def smpp():
	return render_template('smpp.html')

"""@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404"""

class Kannel(Form):
	number = StringField('MSISDN', [validators.Length(max=20)])
	ID = StringField('MessageID', [validators.Length(max=50)])
		
@app.route('/Kannel', methods=['GET','POST'])
def kannel():
	form = Kannel(request.form)
	if request.method == 'POST' and form.validate():
		number = request.form['number']
		ID = request.form['ID']
		res = search(number)
		session['number'] = number
		session['res'] = res
		return redirect(url_for('result', res=res))
	else:		
		return render_template('kannel.html', form=form)

@app.route('/result', methods=['GET', 'POST'])
def result():
	#data = kannel(request.res)
	return render_template('result.html')

if __name__ == '__main__':
	app.secret_key='ceq134'
	app.run(debug=True)