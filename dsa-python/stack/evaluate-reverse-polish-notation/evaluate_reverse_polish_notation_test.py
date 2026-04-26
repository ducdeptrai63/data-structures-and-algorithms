import unittest

from evaluate_reverse_polish_notation import Solution


class TestEvaluateReversePolishNotation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_operations(self):
        self.assertEqual(self.solution.evalRPN(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(self.solution.evalRPN(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(self.solution.evalRPN(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)

    def test_mixed_operations(self):
        self.assertEqual(self.solution.evalRPN(
            ["5", "1", "2", "+", "4", "*", "+", "3", "-"]), 14)

    def test_negative_numbers(self):
        self.assertEqual(self.solution.evalRPN(["-2", "-3", "*"]), 6)
        self.assertEqual(self.solution.evalRPN(["-10", "5", "-"]), -15)
        self.assertEqual(self.solution.evalRPN(["-10", "-5", "-"]), -5)
        self.assertEqual(self.solution.evalRPN(["5", "-10", "+"]), -5)

    def test_division_truncation_toward_zero(self):
        self.assertEqual(self.solution.evalRPN(["13", "5", "/"]), 2)
        self.assertEqual(self.solution.evalRPN(["-13", "5", "/"]), -2)
        self.assertEqual(self.solution.evalRPN(["13", "-5", "/"]), -2)
        self.assertEqual(self.solution.evalRPN(["-13", "-5", "/"]), 2)
        self.assertEqual(self.solution.evalRPN(["6", "-100", "/"]), 0)

    def test_minimum_input_size(self):
        self.assertEqual(self.solution.evalRPN(["18"]), 18)
        self.assertEqual(self.solution.evalRPN(["-100"]), -100)
        self.assertEqual(self.solution.evalRPN(["0"]), 0)

    def test_maximum_input_size(self):
        tokens_add = ["1"] * 500 + ["+"] * 499
        self.assertEqual(self.solution.evalRPN(tokens_add), 500)

        tokens_mult = ["-1"] * 500 + ["*"] * 499
        self.assertEqual(self.solution.evalRPN(tokens_mult), 1)


if __name__ == '__main__':
    unittest.main()
