import unittest

from lemonade_change import Solution


class TestLemonadeChange(unittest.TestCase):
    def setUp(self) -> None:
        self.sln = Solution()

    def test_single_five_true(self):
        self.assertTrue(self.sln.lemonadeChange([5]))

    def test_all_fives_true(self):
        self.assertTrue(self.sln.lemonadeChange([5, 5, 5, 5, 5, 5]))

    def test_first_bill_ten_false(self):
        self.assertFalse(self.sln.lemonadeChange([10]))

    def test_first_bill_twenty_false(self):
        self.assertFalse(self.sln.lemonadeChange([20]))

    def test_example_true(self):
        self.assertTrue(self.sln.lemonadeChange([5, 5, 5, 10, 20]))

    def test_example_false_due_to_missing_five(self):
        self.assertFalse(self.sln.lemonadeChange([5, 5, 10, 10, 20]))

    def test_twenty_uses_three_fives_when_no_ten(self):
        # After three 5s, a 20 can be changed using 5+5+5.
        self.assertTrue(self.sln.lemonadeChange([5, 5, 5, 20]))

    def test_twenty_requires_ten_and_five_preferred_when_possible(self):
        # Build up both 10 and 5, then ensure 20s can be served via 10+5.
        self.assertTrue(self.sln.lemonadeChange([5, 5, 5, 10, 5, 10, 20, 20]))

    def test_mixed_sequence_failure_late(self):
        # Have some change, but run out of 5s for a later 10.
        self.assertFalse(self.sln.lemonadeChange([5, 10, 5, 10, 10]))

    def test_multiple_twenties_with_exact_change(self):
        # After creating 2 tens and 2 fives, serve two 20s using 10+5 twice.
        self.assertFalse(self.sln.lemonadeChange([5, 5, 5, 10, 10, 20, 20]))

    def test_large_input_max_len_success(self):
        # Length = 100000; should run fast and succeed.
        bills = [5] * 50000 + [10] * 25000 + [20] * 25000
        self.assertEqual(len(bills), 100000)
        self.assertTrue(self.sln.lemonadeChange(bills))


if __name__ == "__main__":
    unittest.main()
