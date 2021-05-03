class Pace:
    """Class responsible for controlling game pace.

    Attributes:
        counter (int):
            Helper variable to calculate if game pace should be
            increased or not.
        integer (int):
            Another helper variable to calculate if game pace should be
            increased or not.
        difficulty (int):
            Defines how fast the block falls.
        go_fast (bool):
            Boolean value for momentarily speeding up the game pace.
    """
    def __init__(self):
        """Constructor creates a new Pace object and calls reset_pace method to set attributes.
        """
        self.reset_pace()

    def check_counter(self) -> bool:
        """Checks if counter value has 

        Returns:
            bool: [description]
        """
        self.__increase_counter()
        if self.__counter // 60 > self.__integer:
            self.__integer += 1
            return True
        return False

    def __increase_counter(self):
        if self.__go_fast:
            self.__counter += self.__difficulty * 4
        else:
            self.__counter += self.__difficulty

    def increase_speed(self):
        self.__go_fast = True

    def decrease_speed(self):
        self.__go_fast = False

    def increase_difficulty(self):
        self.__difficulty += 1

    def reset_pace(self):
        self.__counter = 0
        self.__integer = 0
        self.__difficulty = 1
        self.__go_fast = False
