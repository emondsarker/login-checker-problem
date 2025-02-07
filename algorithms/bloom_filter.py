"""
This module provides a Bloom filter implementation for probabilistic set membership testing.
The Bloom filter offers constant-time lookups with a possibility of false positives but no false negatives.
"""

from typing import List


class BloomFilter:
    """
    A Bloom filter implementation using three hash functions.
    
    This class provides probabilistic set membership testing with O(1) lookups.
    False positives are possible, but false negatives are not.
    Space complexity is O(m) where m is size of the bit array (typically m = 10n where n is input size).
    """
    
    def __init__(self, arr: List[str]) -> None:
        """
        Initialize the Bloom filter with a list of strings.
        
        Args:
            arr: List of strings to add to the filter
            
        Time Complexity: O(n) where n is len(arr)
        Space Complexity: O(m) where m is self.size
        """
        self.size = len(arr) * 10  # Size of bit array (m = 10n)
        self.bit_array = [0] * self.size
        
        for item in arr:
            self._add(item)
    
    def _hash1(self, item: str) -> int:
        """First hash function."""
        return hash(item) % self.size
    
    def _hash2(self, item: str) -> int:
        """Second hash function."""
        return hash(item * 2) % self.size
    
    def _hash3(self, item: str) -> int:
        """Third hash function."""
        return hash(item * 3) % self.size
    
    def _add(self, item: str) -> None:
        """
        Add an item to the Bloom filter.
        
        Args:
            item: String to add to the filter
            
        Time Complexity: O(k) where k is number of hash functions (3 in this case)
        """
        self.bit_array[self._hash1(item)] = 1
        self.bit_array[self._hash2(item)] = 1
        self.bit_array[self._hash3(item)] = 1
    
    def search(self, target: str) -> int:
        """
        Check if a target string might be in the set.
        
        Args:
            target: String to search for
            
        Returns:
            int: 1 if the target might be in the set, -1 if definitely not in the set
            
        Time Complexity: O(k) where k is number of hash functions (3 in this case)
        """
        if (self.bit_array[self._hash1(target)] and 
            self.bit_array[self._hash2(target)] and 
            self.bit_array[self._hash3(target)]):
            return 1
        return -1
