"""
Unit tests for the Cuckoo filter implementation.
Tests include performance measurements, correctness verification, and false positive analysis.
"""

import unittest
import random
import time
import sys
import os
from typing import Callable, Any

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.cuckoo_filter import CuckooFilter


def log_runtime(func: Callable) -> Callable:
    """
    Decorator to measure and log the runtime of test methods.
    
    Args:
        func: The test method to measure
        
    Returns:
        Wrapped function that logs runtime information
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = end_time - start_time
        print(f"{func.__name__} runtime: {runtime:.6f} seconds \n\n")
        return result
    return wrapper


class TestCuckooFilter(unittest.TestCase):
    """Test suite for Cuckoo filter implementation."""
    
    def setUp(self) -> None:
        """
        Test fixture setup.
        Initializes Cuckoo filter and loads dataset.
        """
        self.capacity = 1000
        self.filter = CuckooFilter(capacity=self.capacity)
        with open('dataset.txt', 'r') as file:
            self.dataset = [line.strip() for line in file.readlines()]
    
    @log_runtime
    def test_insert_and_lookup(self) -> None:
        """
        Test insertion and lookup operations.
        Verifies that items can be inserted and then found in the filter.
        """
        test_items = self.dataset[:100]
        for item in test_items:
            success = self.filter.insert(item)
            self.assertTrue(success, f"Failed to insert item: {item}")
            self.assertTrue(item in self.filter, f"Item not found after insertion: {item}")
    
    @log_runtime
    def test_search_interface(self) -> None:
        """
        Test the search method interface.
        Verifies that search returns 1 for potential matches and -1 for definite non-matches.
        """
        test_item = self.dataset[0]
        
        # Test for non-existent item
        result = self.filter.search("nonexistent_item")
        self.assertEqual(result, -1, "Search should return -1 for non-existent item")
        
        # Test for inserted item
        self.filter.insert(test_item)
        result = self.filter.search(test_item)
        self.assertEqual(result, 1, "Search should return 1 for existing item")
    
    @log_runtime
    def test_delete(self) -> None:
        """
        Test deletion operation.
        Verifies that items can be properly deleted from the filter.
        """
        test_item = self.dataset[0]
        
        success = self.filter.insert(test_item)
        self.assertTrue(success, "Failed to insert item for deletion test")
        self.assertTrue(test_item in self.filter, "Item should be in filter after insertion")
        
        success = self.filter.delete(test_item)
        self.assertTrue(success, "Failed to delete item")
        self.assertFalse(test_item in self.filter, "Item should not be in filter after deletion")
    
    @log_runtime
    def test_capacity_limits(self) -> None:
        """
        Test filter capacity limits.
        Verifies that the filter handles capacity constraints appropriately.
        """
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
    def test_false_positives(self) -> None:
        """
        Test false positive rate.
        Verifies that the false positive rate is within acceptable bounds.
        """
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
