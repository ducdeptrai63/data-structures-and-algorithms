import unittest

from implement_queue_using_stacks import MyQueue


class TestMyQueue(unittest.TestCase):

    def setUp(self):
        self.queue = MyQueue()

    def test_basic_push_and_pop(self):
        self.queue.push(1)
        self.queue.push(2)
        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(self.queue.pop(), 1)
        self.assertFalse(self.queue.empty())
        self.assertEqual(self.queue.pop(), 2)
        self.assertTrue(self.queue.empty())

    def test_interleaved_push_pop_peek(self):
        self.queue.push(1)
        self.queue.push(2)
        self.assertEqual(self.queue.pop(), 1)
        self.queue.push(3)
        self.queue.push(4)
        self.assertEqual(self.queue.peek(), 2)
        self.assertEqual(self.queue.pop(), 2)
        self.assertEqual(self.queue.pop(), 3)
        self.assertFalse(self.queue.empty())
        self.assertEqual(self.queue.pop(), 4)
        self.assertTrue(self.queue.empty())

    def test_empty_behavior(self):
        self.assertTrue(self.queue.empty())
        self.queue.push(5)
        self.assertFalse(self.queue.empty())
        self.assertEqual(self.queue.pop(), 5)
        self.assertTrue(self.queue.empty())

    def test_multiple_consecutive_operations(self):
        # The constraint says at most 100 calls, so let's push 50 and pop 50
        for i in range(1, 51):
            # Ensuring values are 1 <= x <= 9
            self.queue.push((i % 9) + 1)

        self.assertFalse(self.queue.empty())

        for i in range(1, 51):
            expected = (i % 9) + 1
            self.assertEqual(self.queue.peek(), expected)
            self.assertEqual(self.queue.pop(), expected)

        self.assertTrue(self.queue.empty())


if __name__ == '__main__':
    unittest.main()
