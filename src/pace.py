class Pace:
    def __init__(self):
        self.__counter = 0
        self.__integer = 0
        self.__difficulty = 1
        self.__go_fast = False

    def check_counter(self):
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
