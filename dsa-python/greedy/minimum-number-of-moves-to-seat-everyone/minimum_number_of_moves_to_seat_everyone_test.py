import unittest

from minimum_number_of_moves_to_seat_everyone import Solution


def expected_min_moves(seats, students):
    s_seats = sorted(seats)
    s_students = sorted(students)
    return sum(abs(a - b) for a, b in zip(s_seats, s_students))


class TestMinimumNumberOfMovesToSeatEveryone(unittest.TestCase):
    def test_boundary_n1_min_values(self):
        seats = [1]
        students = [1]
        expected = expected_min_moves(seats, students)
        self.assertEqual(Solution().minMovesToSeat(
            seats[:], students[:]), expected)

    def test_boundary_n1_max_values(self):
        seats = [100]
        students = [100]
        expected = expected_min_moves(seats, students)
        self.assertEqual(Solution().minMovesToSeat(
            seats[:], students[:]), expected)

    def test_boundary_n1_max_distance(self):
        seats = [1]
        students = [100]
        expected = expected_min_moves(seats, students)
        self.assertEqual(Solution().minMovesToSeat(
            seats[:], students[:]), expected)

    def test_already_aligned_zero_moves(self):
        seats = [3, 1, 5, 2, 4]
        students = [1, 2, 3, 4, 5]
        expected = expected_min_moves(seats, students)
        self.assertEqual(Solution().minMovesToSeat(
            seats[:], students[:]), expected)

    def test_completely_reversed_order(self):
        seats = [1, 2, 3, 4, 5, 6]
        students = [6, 5, 4, 3, 2, 1]
        expected = expected_min_moves(seats, students)
        self.assertEqual(Solution().minMovesToSeat(
            seats[:], students[:]), expected)

    def test_all_students_shifted_by_constant_offset(self):
        seats = [1, 2, 3, 4, 5]
        students = [3, 4, 5, 6, 7]  # offset +2, all within 1..100
        expected = expected_min_moves(seats, students)
        self.assertEqual(Solution().minMovesToSeat(
            seats[:], students[:]), expected)

    def test_duplicate_seat_values(self):
        seats = [2, 2, 2, 2]
        students = [1, 2, 3, 4]
        expected = expected_min_moves(seats, students)
        self.assertEqual(Solution().minMovesToSeat(
            seats[:], students[:]), expected)

    def test_duplicate_student_values(self):
        seats = [1, 2, 3, 4]
        students = [2, 2, 2, 2]
        expected = expected_min_moves(seats, students)
        self.assertEqual(Solution().minMovesToSeat(
            seats[:], students[:]), expected)

    def test_mixed_duplicates(self):
        seats = [1, 1, 3, 3, 5, 5]
        students = [1, 2, 2, 4, 4, 6]
        expected = expected_min_moves(seats, students)
        self.assertEqual(Solution().minMovesToSeat(
            seats[:], students[:]), expected)

    def test_fixed_random_valid_distribution_small(self):
        seats = [10, 1, 25, 40, 7, 60, 33, 18]
        students = [12, 2, 20, 41, 9, 58, 30, 17]
        expected = expected_min_moves(seats, students)
        self.assertEqual(Solution().minMovesToSeat(
            seats[:], students[:]), expected)

    def test_worst_case_distribution_max_n_all_ones_vs_all_hundreds(self):
        seats = [1] * 100
        students = [100] * 100
        expected = expected_min_moves(seats, students)
        self.assertEqual(Solution().minMovesToSeat(
            seats[:], students[:]), expected)

    def test_boundary_n100_already_aligned_range(self):
        seats = list(range(1, 101))
        students = list(range(1, 101))
        expected = expected_min_moves(seats, students)
        self.assertEqual(Solution().minMovesToSeat(
            seats[:], students[:]), expected)

    def test_boundary_n100_extremes_vs_mids(self):
        seats = [1] * 50 + [100] * 50
        students = [50] * 100
        expected = expected_min_moves(seats, students)
        self.assertEqual(Solution().minMovesToSeat(
            seats[:], students[:]), expected)


if __name__ == "__main__":
    unittest.main()
