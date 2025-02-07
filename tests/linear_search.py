"""
Unit tests for the linear search implementation.
Tests include performance measurements and correctness verification.
"""

import unittest
import random
import time
import sys
import os
from typing import Callable, Any

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.linear_search import linear_search


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


class TestLinearSearch(unittest.TestCase):
    """Test suite for linear search implementation."""
    
    def setUp(self) -> None:
        """
        Test fixture setup.
        Loads dataset for linear search testing.
        """
        with open('dataset.txt', 'r') as file:
            self.dataset = [line.strip() for line in file.readlines()]
    
    @log_runtime
    def test_linear_search_found(self) -> None:
        """
        Test searching for an existing element.
        Verifies that the search correctly finds and returns the proper index.
        """
        target = self.dataset[random.randint(0, len(self.dataset) - 1)]
        result = linear_search(self.dataset, target)
        print(f"Test Linear Search Found: target={target}, result={result}")
        self.assertNotEqual(result, -1, "Search should find existing element")
        self.assertEqual(self.dataset[result], target, "Found index should contain target")
    
    @log_runtime
    def test_linear_search_not_found(self) -> None:
        """
        Test searching for a non-existent element.
        Verifies that the search correctly returns -1 for missing elements.
        """
        target = "nonexistent_element"
        result = linear_search(self.dataset, target)
        print(f"Test Linear Search Not Found: target={target}, result={result}")
        self.assertEqual(result, -1, "Search should return -1 for non-existent element")
    
    @log_runtime
    def test_linear_search_empty_string(self) -> None:
        """
        Test searching for an empty string.
        Verifies correct handling of edge cases.
        """
        result = linear_search(self.dataset, "")
        self.assertEqual(result, -1, "Search should handle empty string")
    
    @log_runtime
    def test_linear_search_first_last(self) -> None:
        """
        Test searching for first and last elements.
        Verifies correct handling of boundary elements.
        """
        first = self.dataset[0]
        last = self.dataset[-1]
        
        first_result = linear_search(self.dataset, first)
        self.assertEqual(first_result, 0, "Should find first element")
        
        last_result = linear_search(self.dataset, last)
        self.assertEqual(last_result, len(self.dataset) - 1, "Should find last element")

if __name__ == '__main__':
    unittest.main()
