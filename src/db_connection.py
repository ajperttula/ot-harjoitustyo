import os
import sqlite3


dirname = os.path.dirname(__file__)
connection = sqlite3.connect(os.path.join(dirname, "..", "data", "scores.db"))
connection.isolation_level = None


def get_connection():
    """Returns SQLite database connections

    Returns:
        connection: SQLite database connection
    """
    return connection
