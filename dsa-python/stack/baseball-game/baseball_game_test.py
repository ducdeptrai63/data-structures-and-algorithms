import unittest

from baseball_game import Solution


class TestBaseballGame(unittest.TestCase):
    def test_cal_points_basic_example(self):
        solution = Solution()
        ops = ["5", "2", "C", "D", "+"]
        self.assertEqual(solution.calPoints(ops), 30)

    def test_cal_points_only_numbers(self):
        solution = Solution()
        ops = ["1", "2", "3", "4"]
        self.assertEqual(solution.calPoints(ops), 10)

    def test_cal_points_multiple_plus(self):
        solution = Solution()
        ops = ["1", "2", "+", "+", "+"]
        self.assertEqual(solution.calPoints(ops), 19)

    def test_cal_points_multiple_double(self):
        solution = Solution()
        ops = ["3", "D", "D", "D"]
        self.assertEqual(solution.calPoints(ops), 45)

    def test_cal_points_multiple_cancel(self):
        solution = Solution()
        ops = ["10", "20", "C", "C", "5"]
        self.assertEqual(solution.calPoints(ops), 5)

    def test_cal_points_with_negatives(self):
        solution = Solution()
        ops = ["-5", "4", "D", "C", "+", "10"]
        self.assertEqual(solution.calPoints(ops), 8)


if __name__ == "__main__":
    unittest.main()
