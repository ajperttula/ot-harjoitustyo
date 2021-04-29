from db_connection import get_connection


class ScoreRepository:
    def __init__(self, database):
        self.__database = database

    def save_score(self, score):
        sql = """INSERT INTO scores (score) VALUES (?)"""
        self.__database.execute(sql, [score])

    def get_high_score(self):
        sql = """SELECT score FROM scores ORDER BY score DESC LIMIT 10"""
        result = self.__database.execute(sql).fetchall()
        return result


score_repository = ScoreRepository(get_connection())
