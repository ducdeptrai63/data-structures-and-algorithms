import unittest

from implement_stack_using_queues import MyStack


class TestImplementStackUsingQueues(unittest.TestCase):
    def test_single_push_then_pop(self):
        s = MyStack()
        s.push(5)
        self.assertEqual(s.pop(), 5)
        self.assertTrue(s.empty())

    def test_multiple_push_then_pop_lifo_order(self):
        s = MyStack()
        s.push(1)
        s.push(2)
        s.push(3)

        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.empty())

    def test_interleaving_push_and_pop(self):
        s = MyStack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)

        s.push(3)
        self.assertEqual(s.top(), 3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.empty())

    def test_top_does_not_remove_element(self):
        s = MyStack()
        s.push(4)
        s.push(7)

        self.assertEqual(s.top(), 7)
        self.assertEqual(s.top(), 7)  # still there
        self.assertEqual(s.pop(), 7)

        self.assertEqual(s.top(), 4)
        self.assertEqual(s.pop(), 4)
        self.assertTrue(s.empty())

    def test_empty_returns_correct_boolean(self):
        s = MyStack()
        self.assertTrue(s.empty())

        s.push(8)
        self.assertFalse(s.empty())

        self.assertEqual(s.pop(), 8)
        self.assertTrue(s.empty())

    def test_push_values_at_boundaries_1_and_9(self):
        s = MyStack()
        s.push(1)
        s.push(9)
        self.assertEqual(s.pop(), 9)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.empty())

    def test_sequence_of_operations_near_100_calls(self):
        s = MyStack()

        # 40 pushes with values constrained to 1..9
        pushed = []
        for i in range(1, 41):
            v = ((i - 1) % 9) + 1
            pushed.append(v)
            s.push(v)

        # 10 consecutive tops; should not change the stack
        expected_top = pushed[-1]
        for _ in range(10):
            self.assertEqual(s.top(), expected_top)

        # empties at different times
        self.assertFalse(s.empty())

        # pop 39 values (leave 1)
        for expected in reversed(pushed[1:]):
            self.assertEqual(s.pop(), expected)

        self.assertFalse(s.empty())

        # pop final value
        self.assertEqual(s.pop(), pushed[0])
        self.assertTrue(s.empty())

    def test_multiple_consecutive_top_calls(self):
        s = MyStack()
        s.push(2)
        s.push(5)
        s.push(6)

        self.assertEqual(s.top(), 6)
        self.assertEqual(s.top(), 6)
        self.assertEqual(s.top(), 6)
        self.assertEqual(s.pop(), 6)

    def test_multiple_consecutive_empty_checks(self):
        s = MyStack()

        for _ in range(5):
            self.assertTrue(s.empty())

        s.push(1)
        self.assertFalse(s.empty())
        self.assertFalse(s.empty())

        self.assertEqual(s.pop(), 1)

        for _ in range(3):
            self.assertTrue(s.empty())


if __name__ == "__main__":
    unittest.main()
