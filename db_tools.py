#! usr/bin/env python3

"""
CLI tools to manipulate the database.
"""

import database
import sqlite3
import click

con = sqlite3.connect("todo.db")
c = con.cursor()


def create_table():
	"""
	Creates a new database table
	"""
	c.execute('''
						CREATE TABLE todo_items (id INTEGER PRIMARY KEY, item text, status text, notes text, user text)
						''')
	con.commit()


def reset_database():
	"""
	"""
	pass
