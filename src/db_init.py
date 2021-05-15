from db_connection import get_connection


def drop_table(database):
    """Deletes scores table from the database.

    Args:
        database: SQLite database connection.
    """
    sql = "DROP TABLE IF EXISTS scores"
    database.execute(sql)


def create_table(database):
    """Creates a scores table to database

    Args:
        database: SQlite database connection.
    """
    sql = """CREATE TABLE scores
             (id INTEGER PRIMARY KEY, player TEXT, score INTEGER)"""
    database.execute(sql)


def init_database():
    """Gets database connection, formats the database and creates tables.
    """
    database = get_connection()
    drop_table(database)
    create_table(database)
