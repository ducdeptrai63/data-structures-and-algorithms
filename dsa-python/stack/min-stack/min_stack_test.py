import unittest

from min_stack import MinStack


class TestMinStack(unittest.TestCase):

    def test_basic_operations(self):
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        self.assertEqual(stack.getMin(), -3)
        stack.pop()
        self.assertEqual(stack.top(), 0)
        self.assertEqual(stack.getMin(), -2)

    def test_extreme_values(self):
        stack = MinStack()
        min_val = -2**31
        max_val = 2**31 - 1

        stack.push(max_val)
        self.assertEqual(stack.getMin(), max_val)
        self.assertEqual(stack.top(), max_val)

        stack.push(min_val)
        self.assertEqual(stack.getMin(), min_val)
        self.assertEqual(stack.top(), min_val)

        stack.pop()
        self.assertEqual(stack.getMin(), max_val)
        self.assertEqual(stack.top(), max_val)

    def test_multiple_identical_minimum_values(self):
        stack = MinStack()
        stack.push(4)
        stack.push(2)
        stack.push(2)
        stack.push(5)

        self.assertEqual(stack.getMin(), 2)
        stack.pop()  # pop 5
        self.assertEqual(stack.getMin(), 2)
        stack.pop()  # pop 2
        self.assertEqual(stack.getMin(), 2)
        stack.pop()  # pop 2
        self.assertEqual(stack.getMin(), 4)
        self.assertEqual(stack.top(), 4)

    def test_strictly_increasing_sequence(self):
        stack = MinStack()
        for i in range(1, 6):
            stack.push(i)
            self.assertEqual(stack.getMin(), 1)
            self.assertEqual(stack.top(), i)

        for i in range(5, 0, -1):
            self.assertEqual(stack.top(), i)
            self.assertEqual(stack.getMin(), 1)
            stack.pop()

    def test_strictly_decreasing_sequence(self):
        stack = MinStack()
        for i in range(5, 0, -1):
            stack.push(i)
            self.assertEqual(stack.getMin(), i)
            self.assertEqual(stack.top(), i)

        for i in range(1, 6):
            self.assertEqual(stack.top(), i)
            self.assertEqual(stack.getMin(), i)
            stack.pop()

    def test_interleaved_push_and_pop_operations(self):
        stack = MinStack()
        stack.push(10)
        self.assertEqual(stack.getMin(), 10)

        stack.push(20)
        self.assertEqual(stack.getMin(), 10)
        self.assertEqual(stack.top(), 20)

        stack.pop()
        self.assertEqual(stack.getMin(), 10)
        self.assertEqual(stack.top(), 10)

        stack.push(5)
        self.assertEqual(stack.getMin(), 5)
        self.assertEqual(stack.top(), 5)

        stack.push(30)
        self.assertEqual(stack.getMin(), 5)
        self.assertEqual(stack.top(), 30)

        stack.pop()
        self.assertEqual(stack.getMin(), 5)
        self.assertEqual(stack.top(), 5)

        stack.pop()
        self.assertEqual(stack.getMin(), 10)
        self.assertEqual(stack.top(), 10)


if __name__ == '__main__':
    unittest.main()
