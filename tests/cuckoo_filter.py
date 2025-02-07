import unittest
import random
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.cuckoo_filter import CuckooFilter

class TestCuckooFilter(unittest.TestCase):
    def setUp(self):
        self.capacity = 1000
        self.filter = CuckooFilter(capacity=self.capacity)
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
    def test_insert_and_lookup(self):
        test_items = self.dataset[:100]  
        for item in test_items:
            success = self.filter.insert(item)
            self.assertTrue(success, f"Failed to insert item: {item}")
            self.assertTrue(item in self.filter, f"Item not found after insertion: {item}")

    @log_runtime
    def test_delete(self):
        test_item = self.dataset[0]
        
        success = self.filter.insert(test_item)
        self.assertTrue(success, "Failed to insert item for deletion test")
        self.assertTrue(test_item in self.filter)
        
        success = self.filter.delete(test_item)
        self.assertTrue(success, "Failed to delete item")
        self.assertFalse(test_item in self.filter)

    @log_runtime
    def test_capacity_limits(self):
        inserted_count = 0
        max_test_items = self.capacity * 2  
        
        for i in range(max_test_items):
            if self.filter.insert(f"test_item_{i}"):
                inserted_count += 1
            else:
                break
        
        print(f"Successfully inserted {inserted_count} items before filter was full")
        self.assertGreater(inserted_count, 0, "Should be able to insert some items")
        self.assertLess(inserted_count, max_test_items, "Should not be able to insert more than capacity")

    @log_runtime
    def test_false_positives(self):
        test_items = self.dataset[:100]
        for item in test_items:
            self.filter.insert(item)
        
        false_positives = 0
        test_size = 1000
        for i in range(test_size):
            test_item = f"definitely_not_inserted_{i}"
            if test_item in self.filter:
                false_positives += 1
        
        false_positive_rate = false_positives / test_size
        print(f"False positive rate: {false_positive_rate:.4f}")
        self.assertLess(false_positive_rate, 0.1, "False positive rate should be reasonable")

if __name__ == '__main__':
    unittest.main()
