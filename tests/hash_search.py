import unittest
import random
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.hash_search import hash_search

class TestHashSearch(unittest.TestCase):
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

    @log_runtime
    def test_hash_search_found(self):
        target = self.dataset[random.randint(0, len(self.dataset) - 1)]
        result = hash_search(self.dataset, target)
        print(f"Test Hash Search Found: target={target}, result={result}")
        self.assertNotEqual(result, -1)
        self.assertEqual(self.dataset[result], target)

    @log_runtime
    def test_hash_search_not_found(self):
        target = "nonexistent_element"
        result = hash_search(self.dataset, target)
        print(f"Test Hash Search Not Found: target={target}, result={result}")
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
