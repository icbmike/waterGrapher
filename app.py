import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html')

@app.route("/<name>/")
def name(name):
	return "Hello " + name

if __name__ == '__main__':
	app.run()