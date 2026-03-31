import heapq
import random
import unittest

from kth_largest_element_in_a_stream import KthLargest


def kth_largest_reference(values, k):
    if not values:
        raise ValueError("reference requires at least one value")
    if len(values) < k:
        return min(values)
    return sorted(values)[-k]


class TestKthLargest(unittest.TestCase):
    def test_empty_initial_nums_k_1(self):
        kth = KthLargest(1, [])
        seen = []
        for val in [5, -1, 5, 2, -10, 7, 7, 0]:
            seen.append(val)
            got = kth.add(val)
            self.assertEqual(got, kth_largest_reference(seen, 1))

    def test_k_equals_1_typical(self):
        nums = [4, -2, 4, 3]
        kth = KthLargest(1, nums)
        seen = list(nums)

        for val in [-5, 10, 10, 0, 9]:
            seen.append(val)
            got = kth.add(val)
            self.assertEqual(got, kth_largest_reference(seen, 1))

    def test_k_equals_nums_length(self):
        nums = [3, 1, 2, 2, -1]
        k = len(nums)
        kth = KthLargest(k, nums)
        seen = list(nums)

        for val in [0, -10, 5, 2]:
            seen.append(val)
            got = kth.add(val)
            self.assertEqual(got, kth_largest_reference(seen, k))

    def test_k_equals_nums_length_plus_one(self):
        nums = [5, 2, 4]
        k = len(nums) + 1
        kth = KthLargest(k, nums)
        seen = list(nums)

        for val in [3, 10, 1, 6]:
            seen.append(val)
            got = kth.add(val)
            self.assertEqual(got, kth_largest_reference(seen, k))

    def test_negative_values_and_duplicates(self):
        nums = [-1, -1, -2, -3, -3]
        k = 3
        kth = KthLargest(k, nums)
        seen = list(nums)

        for val in [-4, -1, -2, -10, -3]:
            seen.append(val)
            got = kth.add(val)
            self.assertEqual(got, kth_largest_reference(seen, k))

    def test_increasing_sequence(self):
        nums = [1, 2, 3, 4, 5]
        k = 2
        kth = KthLargest(k, nums)
        seen = list(nums)

        for val in [6, 7, 8, 9]:
            seen.append(val)
            got = kth.add(val)
            self.assertEqual(got, kth_largest_reference(seen, k))

    def test_decreasing_sequence(self):
        nums = [9, 8, 7, 6, 5]
        k = 4
        kth = KthLargest(k, nums)
        seen = list(nums)

        for val in [4, 3, 2, 1, 0]:
            seen.append(val)
            got = kth.add(val)
            self.assertEqual(got, kth_largest_reference(seen, k))

    def test_multiple_consecutive_add_calls_validate_each_return(self):
        nums = [4, 5, 8, 2]
        k = 3
        kth = KthLargest(k, nums)
        seen = list(nums)

        adds = [3, 5, 10, 9, 4]
        for val in adds:
            seen.append(val)
            got = kth.add(val)
            self.assertEqual(got, kth_largest_reference(seen, k))

    def test_large_input_stress_with_checkpoints(self):
        rng = random.Random(1337)

        n = 10_000
        nums = [rng.randint(-10_000, 10_000) for _ in range(n)]
        k = 257

        kth = KthLargest(k, nums)

        all_seen = list(nums)

        expected_heap = list(nums)
        heapq.heapify(expected_heap)
        while len(expected_heap) > k:
            heapq.heappop(expected_heap)

        m = 1_000
        checkpoints = set(list(range(0, m, 97)) + [m - 1])

        for i in range(m):
            val = rng.randint(-10_000, 10_000)
            all_seen.append(val)

            got = kth.add(val)

            heapq.heappush(expected_heap, val)
            if len(expected_heap) > k:
                heapq.heappop(expected_heap)
            self.assertEqual(got, expected_heap[0])

            if i in checkpoints:
                self.assertEqual(got, kth_largest_reference(all_seen, k))

        self.assertTrue(len(all_seen) <= 11_000)


if __name__ == "__main__":
    unittest.main()
