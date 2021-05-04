class Score:
    """Class responsible for counting game score.

    In addition to counting score, each time rows are deleted,
    counter value is added by one.
    Note that deleting multiple rows at once is still one occurence.

    Attributes:
        score (int): Value for game score.
        counter (int): Value for determining, if game difficulty should be increased.
    """
    def __init__(self):
        """Constructor creates a new Score object
        """
        self.score = 0
        self.__counter = 0

    def add_score(self, points: int):
        """Adds score based on full rows deleted.

        Args:
            points (int): Number of full rows deleted.
        """
        self.score += points
        self.__increase_counter()

    def __increase_counter(self):
        """Increases counter value by one.
        """
        self.__counter += 1

    def check_score(self) -> bool:
        """Checks if 15 deletion events have occured.

        If counter reaches 15, function calls reset_counter to
        set counter to zero.

        Returns:
            bool: True if counter equals 15, else False.
        """
        if self.__counter == 15:
            self.__reset_counter()
            return True
        return False

    def __reset_counter(self):
        """Sets counter value to zero.
        """
        self.__counter = 0

    def reset_score(self):
        """Resets score and counter values to zero.
        """
        self.score = 0
        self.__counter = 0
