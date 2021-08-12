#! usr/bin/env python3

"""
"""

import sqlite3


class Database:
	
	
	def __init__(self):
		"""
		"""
		self.con = sqlite3.connect("todo.db")
		self.c = con.cursor()
		self.results = None

	
	def create_item(self, item_name: str):
		"""
		"""
		self.c.execute()
		self._commit()
	
	
	def read_items(self):
		"""
		"""
		self.c.execute()
	
	
	def update(self):
		"""
		"""
		self.c.execute()
		self._commit()
	
	
	def delete(self):
		"""
		"""
		self.c.execute()
		self._commit()
	
	
	def _commit(self):
		"""
		Commits changes; wrapper to comply with DRY principle.
		"""
		self.con.commit()
