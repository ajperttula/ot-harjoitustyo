import unittest
from pace import Pace


class TestPace(unittest.TestCase):
    def setUp(self):
        self.pace = Pace()

    def test_constructor_sets_counter_to_zero(self):
        self.assertEqual(self.pace._Pace__counter, 0)

    def test_constructor_sets_integer_to_zero(self):
        self.assertEqual(self.pace._Pace__integer, 0)

    def test_constructor_sets_right_initial_difficulty(self):
        self.assertEqual(self.pace._Pace__difficulty, 2)

    def test_constructor_sets_go_fast_false(self):
        self.assertFalse(self.pace._Pace__go_fast)

    def test_increase_counter_adds_difficulty_to_counter_when_go_fast_false(self):
        self.pace.increase_counter()
        self.assertEqual(self.pace._Pace__counter, 2)

    def test_increase_counter_adds_multiplied_difficulty_to_counter_when_go_fast_true(self):
        self.pace.increase_speed()
        self.pace.increase_counter()
        self.assertEqual(self.pace._Pace__counter, 8)

    def test_check_counter_adds_integer_value_by_one_when_floor_divide_result_greater_than_integer(self):
        for i in range(60):
            self.pace.increase_counter()
        self.pace.check_counter()
        self.assertEqual(self.pace._Pace__integer, 1)

    def test_check_counter_returns_true_when_floor_divide_result_greater_than_integer(self):
        for i in range(60):
            self.pace.increase_counter()
        self.assertTrue(self.pace.check_counter())

    def test_check_counter_doesnt_change_integer_value_when_floor_divide_result_less_than_integer(self):
        self.pace.increase_counter()
        self.pace.check_counter()
        self.assertEqual(self.pace._Pace__integer, 0)

    def test_check_counter_returns_false_when_floor_divide_result_less_than_integer(self):
        self.pace.increase_counter()
        self.assertFalse(self.pace.check_counter())

    def test_increase_speed_sets_go_fast_true(self):
        self.pace.increase_speed()
        self.assertTrue(self.pace._Pace__go_fast)

    def test_decrease_speed_sets_go_fast_false(self):
        self.pace.increase_speed()
        self.pace.decrease_speed()
        self.assertFalse(self.pace._Pace__go_fast)
