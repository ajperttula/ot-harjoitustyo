import os
import sqlite3


dirname = os.path.dirname(__file__)
connection = sqlite3.connect(os.path.join(dirname, "data", "scores.db"))
connection.isolation_level = None
connection.row_factory = sqlite3.Row


def get_connection():
    return connection
