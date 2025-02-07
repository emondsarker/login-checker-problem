"""
This module provides a linear search algorithm with O(n) time complexity.
"""

from typing import List


class LinearSearch:
    """
    A linear search implementation that provides sequential lookups.
    
    This class stores an array and performs linear search for O(n) lookups.
    The space complexity is O(1) as it only stores references to the input array.
    """
    
    def __init__(self, arr: List[str]) -> None:
        """
        Initialize with the input array.
        
        Args:
            arr: List of strings to be searched through
            
        Time Complexity: O(1) for initialization
        Space Complexity: O(1) for storing array reference
        """
        self.arr = arr
    
    def search(self, target: str) -> int:
        """
        Search for a target string using linear search.
        
        Args:
            target: String to search for
            
        Returns:
            int: Index of the target in the array, or -1 if not found
            
        Time Complexity: O(n) where n is the array length
        """
        for i in range(len(self.arr)):
            if self.arr[i] == target:
                return i
        return -1
