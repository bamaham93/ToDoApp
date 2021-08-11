#! usr/bin/env python3

"""
"""


from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

database_result = [[["Install aileron"],["Not Done"],["Need help"]], [["Fix WO for N4837A"],["Not Done"],["See GJ"]]]


@app.route('/', methods=['GET'])
def home():
	"""
	"""
	return render_template("home.html", username="Jacob", todos=database_result)


if __name__ == '__main__':
	app.run()
	
	"{?p;.juy6rt}"
