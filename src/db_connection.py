import os
import sqlite3
from config import DATABASE_FILENAME


dirname = os.path.dirname(__file__)
connection = sqlite3.connect(os.path.join(dirname, "..", "data", DATABASE_FILENAME))
connection.isolation_level = None


def get_connection():
    """Returns SQLite database connections

    Returns:
        connection: SQLite database connection
    """
    return connection
