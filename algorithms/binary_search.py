"""
This module provides a binary search algorithm with O(log n) time complexity.
"""

from typing import List


class BinarySearch:
    """
    A binary search implementation that provides logarithmic-time lookups.
    
    This class stores a sorted array and performs binary search for O(log n) lookups.
    The space complexity is O(1) as it only stores references to the input array.
    """
    
    def __init__(self, arr: List[str]) -> None:
        """
        Initialize with the sorted input array.
        
        Args:
            arr: Sorted list of strings to be searched through
            
        Time Complexity: O(1) for initialization
        Space Complexity: O(1) for storing array reference
        """
        self.arr = arr
    
    def search(self, target: str) -> int:
        """
        Search for a target string using binary search.
        
        Args:
            target: String to search for
            
        Returns:
            int: Index of the target in the array, or -1 if not found
            
        Time Complexity: O(log n) where n is the array length
        """
        left, right = 0, len(self.arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
