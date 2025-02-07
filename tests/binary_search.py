"""
Unit tests for the binary search implementation.
Tests include performance measurements and correctness verification.
Requires sorted dataset for correct functionality.
"""

import os
import sys
import unittest
import time
import random
from typing import Callable, Any

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.binary_search import binary_search


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


class TestBinarySearch(unittest.TestCase):
    """Test suite for binary search implementation."""
    
    def setUp(self) -> None:
        """
        Test fixture setup.
        Loads sorted dataset for binary search testing.
        """
        with open('sorted_dataset.txt', 'r') as file:
            self.dataset = [line.strip() for line in file.readlines()]
    
    @log_runtime
    def test_binary_search_found(self) -> None:
        """
        Test searching for an existing element.
        Verifies that the search correctly finds and returns the proper index.
        """
        target = self.dataset[random.randint(0, len(self.dataset) - 1)]
        result = binary_search(self.dataset, target)
        print(f"Test Binary Search Found: target={target}, result={result}")
        self.assertNotEqual(result, -1, "Search should find existing element")
        self.assertEqual(self.dataset[result], target, "Found index should contain target")
    
    @log_runtime
    def test_binary_search_not_found(self) -> None:
        """
        Test searching for a non-existent element.
        Verifies that the search correctly returns -1 for missing elements.
        """
        target = "nonexistent_element"
        result = binary_search(self.dataset, target)
        print(f"Test Binary Search Not Found: target={target}, result={result}")
        self.assertEqual(result, -1, "Search should return -1 for non-existent element")
    
    @log_runtime
    def test_binary_search_empty_string(self) -> None:
        """
        Test searching for an empty string.
        Verifies correct handling of edge cases.
        """
        result = binary_search(self.dataset, "")
        self.assertEqual(result, -1, "Search should handle empty string")
    
    @log_runtime
    def test_binary_search_first_last(self) -> None:
        """
        Test searching for first and last elements.
        Verifies correct handling of boundary elements.
        """
        first = self.dataset[0]
        last = self.dataset[-1]
        
        first_result = binary_search(self.dataset, first)
        self.assertEqual(first_result, 0, "Should find first element")
        
        last_result = binary_search(self.dataset, last)
        self.assertEqual(last_result, len(self.dataset) - 1, "Should find last element")

if __name__ == '__main__':
    unittest.main()
