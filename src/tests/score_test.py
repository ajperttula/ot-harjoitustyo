import unittest
from game_loop.score import Score


class TestScore(unittest.TestCase):
    def setUp(self):
        self.score = Score()

    def test_constructor_sets_score_to_zero(self):
        self.assertEqual(self.score.score, 0)

    def test_constructor_sets_counter_to_zero(self):
        self.assertEqual(self.score._Score__counter, 0)

    def test_add_score_adds_points_given_as_argument_to_score(self):
        self.score.add_score(5)
        self.assertEqual(self.score.score, 5)

    def test_add_score_adds_points_by_one(self):
        self.score.add_score(5)
        self.assertEqual(self.score._Score__counter, 1)

    def test_check_score_resets_counter_if_counter_eq_15(self):
        for i in range(15):
            self.score.add_score(1)
        self.score.check_score()
        self.assertEqual(self.score._Score__counter, 0)

    def test_check_score_doesnt_reset_counter_if_counter_lt_15(self):
        for i in range(5):
            self.score.add_score(1)
        self.score.check_score()
        self.assertEqual(self.score._Score__counter, 5)

    def test_check_score_returns_true_if_counter_eq_15(self):
        for i in range(15):
            self.score.add_score(1)
        self.assertTrue(self.score.check_score())

    def test_check_score_returns_false_if_counter_lt_15(self):
        self.score.add_score(1)
        self.assertFalse(self.score.check_score())
