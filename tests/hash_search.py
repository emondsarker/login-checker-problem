"""
Unit tests for the hash-based search implementation.
Tests include performance measurements and correctness verification.
"""

import unittest
import random
import time
import sys
import os
from typing import Callable, Any

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.hash_search import HashSearch


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


class TestHashSearch(unittest.TestCase):
    """Test suite for HashSearch implementation."""
    
    def setUp(self) -> None:
        """
        Test fixture setup.
        Loads dataset and initializes HashSearch instance.
        """
        with open('dataset.txt', 'r') as file:
            self.dataset = [line.strip() for line in file.readlines()]
            self.hash_table = HashSearch(self.dataset)
            self.hash_search = self.hash_table.search
    
    @log_runtime
    def test_hash_search_found(self) -> None:
        """
        Test searching for an existing element.
        Verifies that the search correctly finds and returns the proper index.
        """
        target = self.dataset[random.randint(0, len(self.dataset) - 1)]
        result = self.hash_search(target)
        print(f"Test Hash Search Found: target={target}, result={result}")
        self.assertNotEqual(result, -1, "Search should find existing element")
        self.assertEqual(self.dataset[result], target, "Found index should contain target")
    
    @log_runtime
    def test_hash_search_not_found(self) -> None:
        """
        Test searching for a non-existent element.
        Verifies that the search correctly returns -1 for missing elements.
        """
        target = "nonexistent_element"
        result = self.hash_search(target)
        print(f"Test Hash Search Not Found: target={target}, result={result}")
        self.assertEqual(result, -1, "Search should return -1 for non-existent element")
    
    @log_runtime
    def test_hash_search_empty_string(self) -> None:
        """
        Test searching for an empty string.
        Verifies correct handling of edge cases.
        """
        result = self.hash_search("")
        self.assertEqual(result, -1, "Search should handle empty string")
    
    @log_runtime
    def test_hash_search_first_last(self) -> None:
        """
        Test searching for first and last elements.
        Verifies correct handling of boundary elements.
        """
        first = self.dataset[0]
        last = self.dataset[-1]
        
        first_result = self.hash_search(first)
        self.assertEqual(first_result, 0, "Should find first element")
        
        last_result = self.hash_search(last)
        self.assertEqual(last_result, len(self.dataset) - 1, "Should find last element")

if __name__ == '__main__':
    unittest.main()
