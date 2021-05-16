class Pace:
    """Class responsible for controlling game pace.

    This class controls the pace which block falls from the starting position.
    Instead of constant movement, block falls one grid cell at a time starting
    at a pace of one cell per second.

    Attributes:
        counter (int):
            Helper variable to calculate if game pace should be
            increased or not
        integer (int):
            Another helper variable to calculate if game pace should be
            increased or not
        difficulty (int):
            Defines how fast the block falls
        go_fast (bool):
            Boolean value for momentarily speeding up the game pace
    """

    def __init__(self):
        """Creates a new Pace object and sets attributes.
        """
        self.__counter = 0
        self.__integer = 0
        self.__difficulty = 1
        self.__go_fast = False

    def check_counter(self) -> bool:
        """Calls increase_counter and compares counter and integer values.

        Comparison is made by floor dividing counter value by 60 and then
        checking, if it is greater than integer value. If this is true,
        integer value is added by one.

        Returns:
            bool: True or False depending on the equation result
        """
        self.__increase_counter()
        if self.__counter // 60 > self.__integer:
            self.__integer += 1
            return True
        return False

    def __increase_counter(self):
        """Increases counter's value.

        Value is increased by difficulty value, if go_fast is False, or,
        if go_fast is True, value is increased by difficulty times four.
        """
        if self.__go_fast:
            self.__counter += self.__difficulty * 4
        else:
            self.__counter += self.__difficulty

    def increase_speed(self):
        """Sets go_fast True.
        """
        self.__go_fast = True

    def decrease_speed(self):
        """Sets go_fast False.
        """
        self.__go_fast = False

    def increase_difficulty(self):
        """Increases difficulty value by one.
        """
        self.__difficulty += 1

    def reset_pace(self):
        """Resets object attributes.
        """
        self.__counter = 0
        self.__integer = 0
        self.__difficulty = 1
        self.__go_fast = False
