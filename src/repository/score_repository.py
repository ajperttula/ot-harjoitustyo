import sqlite3
from db_connection import get_connection
from db_init import init_database


class ScoreRepository:
    """Class responsible for communicating with SQL database.

    Attributes:
        database: SQL database connection
    """

    def __init__(self, database):
        """Creates a new ScoreRepository and sets attributes.

        Args:
            database: SQL database connection
        """
        self.__database = database
        self.__valid_database()

    def __valid_database(self):
        """Checks if database is alreade initiated.

        If not, calls init_database method to initiate database with correct tables.
        """
        try:
            sql = "SELECT * FROM scores"
            self.__database.execute(sql).fetchall()
        except sqlite3.OperationalError:
            init_database()

    def save_score(self, player: str, score: int):
        """Saves player name and score to database.

        Args:
            player (str): Name given by the player
            score (int): Score achieved
        """
        sql = "INSERT INTO scores (player, score) VALUES (?, ?)"
        self.__database.execute(sql, [player, score])

    def get_high_scores(self):
        """Gets top 10 scores from the database in descending order.

        Returns:
            list: List containing tuples (rank, player, score)
        """
        sql = "SELECT RANK () OVER (ORDER BY score DESC), player, score FROM scores LIMIT 10"
        result = self.__database.execute(sql).fetchall()
        return result

    def delete_data(self):
        """Empties scores table.
        """
        sql = "DELETE FROM scores"
        self.__database.execute(sql)


score_repository = ScoreRepository(get_connection())
