"""
Unit tests for the Bloom filter implementation.
Tests include performance measurements and correctness verification.
"""

import unittest
import random
import time
import sys
import os
from typing import Callable, Any

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.bloom_filter import BloomFilter


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


class TestBloomFilter(unittest.TestCase):
    """Test suite for Bloom filter implementation."""
    
    def setUp(self) -> None:
        """
        Test fixture setup.
        Loads dataset and initializes BloomFilter instance.
        """
        with open('dataset.txt', 'r') as file:
            self.dataset = [line.strip() for line in file.readlines()]
            self.bloom_filter = BloomFilter(self.dataset)
    
    @log_runtime
    def test_bloom_filter_found(self) -> None:
        """
        Test searching for an existing element.
        Verifies that the filter correctly identifies potential matches.
        """
        target = self.dataset[random.randint(0, len(self.dataset) - 1)]
        result = self.bloom_filter.search(target)
        print(f"Test Bloom Filter Found: target={target}, result={result}")
        self.assertEqual(result, 1, "Filter should indicate potential match for existing element")
    
    @log_runtime
    def test_bloom_filter_not_found(self) -> None:
        """
        Test searching for a non-existent element.
        Verifies that the filter correctly identifies definite non-matches.
        """
        target = "nonexistent_element"
        result = self.bloom_filter.search(target)
        print(f"Test Bloom Filter Not Found: target={target}, result={result}")
        self.assertEqual(result, -1, "Filter should indicate definite non-match")
    
    @log_runtime
    def test_bloom_filter_empty_string(self) -> None:
        """
        Test searching for an empty string.
        Verifies correct handling of edge cases.
        """
        result = self.bloom_filter.search("")
        self.assertEqual(result, -1, "Filter should handle empty string")
    
    @log_runtime
    def test_bloom_filter_first_last(self) -> None:
        """
        Test searching for first and last elements.
        Verifies correct handling of boundary elements.
        """
        first = self.dataset[0]
        last = self.dataset[-1]
        
        first_result = self.bloom_filter.search(first)
        self.assertEqual(first_result, 1, "Should find first element")
        
        last_result = self.bloom_filter.search(last)
        self.assertEqual(last_result, 1, "Should find last element")

if __name__ == '__main__':
    unittest.main()
