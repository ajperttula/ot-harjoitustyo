import unittest
from repository.score_repository import score_repository


class TestScoreRepository(unittest.TestCase):
    def setUp(self):
        score_repository.delete_data()
        self.player_name = "John"
        self.score = 5

    def test_save_score_saves_player_name(self):
        score_repository.save_score(self.player_name, self.score)
        result = score_repository.get_high_scores()[0][1]
        self.assertEqual(result, self.player_name)

    def test_save_score_saves_score(self):
        score_repository.save_score(self.player_name, self.score)
        result = score_repository.get_high_scores()[0][2]
        self.assertEqual(result, self.score)

    def test_first_place_rank(self):
        score_repository.save_score(self.player_name, self.score)
        score_repository.save_score("Matt", 4)
        result = score_repository.get_high_scores()[0][0]
        self.assertEqual(result, 1)

    def test_second_place_rank(self):
        score_repository.save_score(self.player_name, self.score)
        score_repository.save_score("Matt", 4)
        result = score_repository.get_high_scores()[1][0]
        self.assertEqual(result, 2)

    def test_equal_rank(self):
        score_repository.save_score(self.player_name, self.score)
        score_repository.save_score("Matt", 5)
        result_1 = score_repository.get_high_scores()[0][0]
        result_2 = score_repository.get_high_scores()[1][0]
        self.assertEqual(result_1, result_2)

    def  test_high_scores_limited_to_10(self):
        for i in range(10):
            score_repository.save_score(self.player_name, self.score)
        score_repository.save_score(self.player_name, 4)
        last_score = score_repository.get_high_scores()[-1][2]
        self.assertEqual(last_score, 5)
