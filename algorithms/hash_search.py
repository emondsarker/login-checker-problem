"""
This module provides a hash table-based search algorithm with O(1) average time complexity.
"""

from typing import List, Dict


class HashSearch:
    """
    A hash table-based search implementation that provides constant-time lookups.
    
    This class creates a hash table from the input array for O(1) average case lookups.
    The space complexity is O(n) where n is the size of the input array.
    """
    
    def __init__(self, arr: List[str]) -> None:
        """
        Initialize the hash table with the input array.
        
        Args:
            arr: List of strings to be searched through
            
        Time Complexity: O(n) for initialization
        Space Complexity: O(n) for hash table storage
        """
        self.hash_table: Dict[str, int] = {item: index for index, item in enumerate(arr)}
    
    def search(self, target: str) -> int:
        """
        Search for a target string in the hash table.
        
        Args:
            target: String to search for
            
        Returns:
            int: Index of the target in the original array, or -1 if not found
            
        Time Complexity: O(1) average case
        """
        return self.hash_table.get(target, -1)
