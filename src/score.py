class Score:
    def __init__(self):
        self.__score = 0
        self.__counter = 0

    def add_score(self, points):
        self.__score += points
        self.__counter += points

    def check_score(self):
        if self.__counter == 15:
            self.__counter = 0
            return True
        return False

    @property
    def score(self):
        return self.__score
