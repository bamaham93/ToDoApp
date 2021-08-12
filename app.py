#! usr/bin/env python3

"""
Simple to do manager app for personal use and learning.
"""


from flask import Flask, render_template, redirect, url_for
#from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

database_results_not_finished = [
																	["Establish world peace", "Not Done", "Might need some help"],
																	["Make billions of dollars", "In progress", "May need some startup capital; $100?"],
																	["Be outragrously generous", "Not Done", "Waiting on task 2"]
																]

database_results_in_progress = [
																	["Phase Inspection on N444AK", "In Progress", ""],
																	["Phase inspection on N353TS", "In Progress", ""],
																	["N241EW Annual", "In Progress", ""],
																]

database_results_finished = [
															["Install aileron","Done","Need help"], ["Fix WO for N4837A", "Done", "See JG"],
															["", "", ""],
															["", "", ""],
														]


@app.route('/', methods=['GET'])
def home():
	"""
	"""
	return render_template("home.html", username="Jacob", done=database_results_finished, not_done=database_results_not_finished, in_progress=database_results_in_progress)


@app.route('/add/<item>', methods=["GET"])
def add_item(item):
	"""
	Validated; just add logic.
	"""
	print(item)
	return redirect(url_for("home"))


if __name__ == '__main__':
	app.run()
