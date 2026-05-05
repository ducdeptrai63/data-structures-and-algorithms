import unittest

from time_based_key_value_store import TimeMap


class TestTimeMap(unittest.TestCase):

    def test_basic_set_and_get(self):
        time_map = TimeMap()
        time_map.set("foo", "bar", 1)
        self.assertEqual(time_map.get("foo", 1), "bar")
        self.assertEqual(time_map.get("foo", 3), "bar")

        time_map.set("foo", "bar2", 4)
        self.assertEqual(time_map.get("foo", 4), "bar2")
        self.assertEqual(time_map.get("foo", 5), "bar2")
        self.assertEqual(time_map.get("foo", 3), "bar")

    def test_get_non_existent_key(self):
        time_map = TimeMap()
        time_map.set("foo", "bar", 1)
        self.assertEqual(time_map.get("baz", 1), "")
        self.assertEqual(time_map.get("baz", 10), "")

    def test_get_timestamp_before_first_set(self):
        time_map = TimeMap()
        time_map.set("foo", "bar", 5)
        self.assertEqual(time_map.get("foo", 1), "")
        self.assertEqual(time_map.get("foo", 4), "")

    def test_multiple_keys(self):
        time_map = TimeMap()
        time_map.set("key1", "value1", 10)
        time_map.set("key2", "value2", 20)

        self.assertEqual(time_map.get("key1", 15), "value1")
        self.assertEqual(time_map.get("key2", 25), "value2")
        self.assertEqual(time_map.get("key1", 5), "")

    def test_boundary_timestamps(self):
        time_map = TimeMap()
        # Minimum timestamp
        time_map.set("min", "val1", 1)
        self.assertEqual(time_map.get("min", 1), "val1")

        # Maximum timestamp based on constraints
        time_map.set("max", "val1000", 1000)
        self.assertEqual(time_map.get("max", 1000), "val1000")
        self.assertEqual(time_map.get("max", 1001), "val1000")

    def test_max_length_key_value(self):
        time_map = TimeMap()
        long_key = "a" * 100
        long_val = "b" * 100
        time_map.set(long_key, long_val, 1)
        self.assertEqual(time_map.get(long_key, 1), long_val)

    def test_alphanumeric_characters(self):
        time_map = TimeMap()
        time_map.set("key123a", "val456b", 10)
        self.assertEqual(time_map.get("key123a", 10), "val456b")

    def test_multiple_updates_same_key(self):
        time_map = TimeMap()
        time_map.set("a", "v1", 10)
        time_map.set("a", "v2", 20)
        time_map.set("a", "v3", 30)
        time_map.set("a", "v4", 40)

        self.assertEqual(time_map.get("a", 5), "")
        self.assertEqual(time_map.get("a", 15), "v1")
        self.assertEqual(time_map.get("a", 20), "v2")
        self.assertEqual(time_map.get("a", 25), "v2")
        self.assertEqual(time_map.get("a", 35), "v3")
        self.assertEqual(time_map.get("a", 45), "v4")


if __name__ == '__main__':
    unittest.main()
