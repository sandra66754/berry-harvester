import unittest
from berry_compressor import sum_for_position, find_max_sum, compress

class TestSumForPosition(unittest.TestCase):
    def test_simple_cyclic(self):
        berries = [1, 2, 3]
        self.assertEqual(sum_for_position(0, berries, 3), 6)
        self.assertEqual(sum_for_position(1, berries, 3), 6)
        self.assertEqual(sum_for_position(2, berries, 3), 6)

    def test_wrap_around(self):
        berries = [10, 20, 30, 40]
        self.assertEqual(sum_for_position(0, berries, 4), 70)
        self.assertEqual(sum_for_position(3, berries, 4), 80)

class TestFindMaxSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(find_max_sum(3, [1, 2, 3]), 6)
        self.assertEqual(find_max_sum(4, [1, 2, 3, 4]), 9)
        self.assertEqual(find_max_sum(5, [5, 1, 1, 1, 5]), 11)

    def test_edge_cases(self):
        self.assertEqual(find_max_sum(3, [100, 1, 1]), 102)
        self.assertEqual(find_max_sum(4, [10, 10, 10, 10]), 30)

class TestCompressIntegration(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(compress([1, 2, 3]), 6)
        self.assertEqual(compress([1, 2, 3, 4]), 9)

if __name__ == "__main__":
    unittest.main()
