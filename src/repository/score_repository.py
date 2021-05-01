from db_connection import get_connection


class ScoreRepository:
    def __init__(self, database):
        self.__database = database

    def save_score(self, player, score):
        sql = """INSERT INTO scores (player, score) VALUES (?, ?)"""
        self.__database.execute(sql, [player, score])

    def get_high_scores(self):
        sql = """SELECT RANK () OVER (ORDER BY score DESC), player, score FROM scores LIMIT 10"""
        result = self.__database.execute(sql).fetchall()
        return result


score_repository = ScoreRepository(get_connection())
