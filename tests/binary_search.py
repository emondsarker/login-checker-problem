import os
import sys
import unittest
import time
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from algorithms.binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        with open('dataset.txt', 'r') as file:
            self.dataset = [line.strip() for line in file.readlines()]

    def log_runtime(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            runtime = end_time - start_time
            print(f"{func.__name__} runtime: {runtime:.6f} seconds \n\n")
            return result
        return wrapper

    def test_found(self):
        arr = [1, 2, 3, 4, 5]
        target = 3
        result = binary_search(arr, target)
        self.assertEqual(result, 2)

    @log_runtime
    def test_binary_search_found(self):
        target = self.dataset[random.randint(0, len(self.dataset) - 1)]
        result = binary_search(self.dataset, target)
        print(f"Test Binary Search Found: target={target}, result={result}")
        self.assertNotEqual(result, -1)
        self.assertEqual(self.dataset[result], target)

    @log_runtime
    def test_binary_search_not_found(self):
        target = "nonexistent_element"
        result = binary_search(self.dataset, target)
        print(f"Test Binary Search Not Found: target={target}, result={result}")
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
