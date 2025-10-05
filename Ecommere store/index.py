from flask import Flask, render_template, request
from random import choice

web_site = Flask(__name__)


@web_site.route('/')
def index():
	return render_template('index.html')

@web_site.route('/productdetail/<var>')
def productdetail(var):
	
    data = ["a","b","c","d"]
    return render_template('productdetail.html',data=data[int(var)])

@web_site.route('/samtv1')
def samtv1():
	return render_template('samtv1.html')

@web_site.route('/samtv2')
def samtv2():
	return render_template('samtv2.html')

@web_site.route('/tcltv1')
def tcltv1():
	return render_template('tcltv1.html')

@web_site.route('/ps501')
def ps501():
	return render_template('ps501.html')

@web_site.route('/ps502')
def ps502():
	return render_template('ps502.html')

@web_site.route('/ps503')
def ps503():
	return render_template('ps503.html')

@web_site.route('/ipad1')
def ipad1():
	return render_template('ipad1.html')

@web_site.route('/ipad2')
def ipad2():
	return render_template('ipad2.html')

@web_site.route('/ipad3')
def ipad3():
	return render_template('ipad3.html')

web_site.run(host='0.0.0.0', port=8080)