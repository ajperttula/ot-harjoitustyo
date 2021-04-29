from db_connection import get_connection


def drop_table(database):
    sql = "DROP TABLE IF EXISTS scores"
    database.execute(sql)


def create_table(database):
    sql = """CREATE TABLE scores
             (id INTEGER PRIMARY KEY, score INTEGER)"""
    database.execute(sql)


def test(database):
    sql = "INSERT INTO scores (score) VALUES (10)"
    database.execute(sql)


def init_database():
    database = get_connection()
    drop_table(database)
    create_table(database)
    test(database)


if __name__ == "__main__":
    init_database()
