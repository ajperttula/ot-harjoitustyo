class Pace:
    def __init__(self):
        self.__counter = 0
        self.__integer = 0
        self.__difficulty = 2
        self.__fast = False

    def increase_counter(self):
        if self.__fast:
            self.__counter += self.__difficulty * 4
        else:
            self.__counter += self.__difficulty

    def check_counter(self):
        if self.__counter // 60 > self.__integer:
            self.__integer += 1
            return True
        return False

    def increase_speed(self):
        self.__fast = True

    def decrease_speed(self):
        self.__fast = False
