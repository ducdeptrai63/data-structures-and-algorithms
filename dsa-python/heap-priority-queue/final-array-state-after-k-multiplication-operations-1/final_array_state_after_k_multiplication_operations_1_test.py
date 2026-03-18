import random
import unittest


from final_array_state_after_k_multiplication_operations_1 import Solution


def reference_final_state(nums, k, multiplier):
    """Brute-force reference based on the statement:

    Repeat k times:
      - choose the smallest value; if tie, choose smallest index
      - multiply it by multiplier
    """

    res = nums[:]
    for _ in range(k):
        i = min(range(len(res)), key=lambda j: (res[j], j))
        res[i] *= multiplier
    return res


class TestFinalArrayStateAfterKMultiplicationOperations1(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_repeated_min_updates(self):
        nums = [1, 2, 3]
        out = self.solution.getFinalState(nums, k=2, multiplier=2)
        self.assertEqual(out, [4, 2, 3])
        self.assertEqual(nums, [1, 2, 3])

    def test_tie_breaks_by_smallest_index(self):
        nums = [5, 5, 6]
        out = self.solution.getFinalState(nums, k=1, multiplier=3)
        self.assertEqual(out, [15, 5, 6])

    def test_k_zero_returns_copy_and_does_not_mutate_input(self):
        nums = [2, 1, 2]
        nums_before = nums[:]
        out = self.solution.getFinalState(nums, k=0, multiplier=99)
        self.assertEqual(out, nums_before)
        self.assertIsNot(out, nums)
        self.assertEqual(nums, nums_before)

    def test_multiplier_one_keeps_array_unchanged_even_after_many_ops(self):
        nums = [3, 1, 2, 1]
        out = self.solution.getFinalState(nums, k=50, multiplier=1)
        self.assertEqual(out, nums)

    def test_multiplier_zero_sticks_to_same_index_after_first_zero(self):
        nums = [4, 2, 3]
        # Step 1: pick index 1 -> 0; subsequent steps keep picking index 1
        out = self.solution.getFinalState(nums, k=3, multiplier=0)
        self.assertEqual(out, [4, 0, 3])

    def test_negative_numbers_work_correctly(self):
        nums = [-1, 2, -3]
        out = self.solution.getFinalState(nums, k=2, multiplier=2)
        self.assertEqual(out, [-1, 2, -12])

    def test_negative_multiplier_can_flip_sign_and_affect_future_minimum(self):
        nums = [2, 3]
        out = self.solution.getFinalState(nums, k=3, multiplier=-1)
        self.assertEqual(out, [-2, 3])

    def test_single_element(self):
        nums = [7]
        out = self.solution.getFinalState(nums, k=4, multiplier=3)
        self.assertEqual(out, [7 * (3**4)])

    def test_randomized_against_reference(self):
        rng = random.Random(0)

        for _ in range(300):
            n = rng.randint(1, 6)
            nums = [rng.randint(-3, 3) for _ in range(n)]
            k = rng.randint(0, 15)
            multiplier = rng.randint(-2, 3)

            nums_before = nums[:]
            expected = reference_final_state(nums, k, multiplier)
            actual = self.solution.getFinalState(nums, k, multiplier)

            self.assertEqual(actual, expected)
            self.assertEqual(nums, nums_before)


if __name__ == "__main__":
    unittest.main()
