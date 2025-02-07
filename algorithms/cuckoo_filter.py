"""
This module provides a Cuckoo filter implementation for approximate set membership testing.
The Cuckoo filter offers constant-time insertions, deletions, and lookups with better space efficiency
than Bloom filters and support for deletion operations.
"""

import hashlib
from typing import List, Optional, Any


class CuckooFilter:
    """
    A Cuckoo filter implementation using two hash tables and buckets.
    
    This class provides approximate set membership testing with O(1) operations.
    Like Bloom filters, false positives are possible but false negatives are not.
    Unlike Bloom filters, Cuckoo filters support deletion and have better space efficiency.
    
    Space complexity is O(n) where n is the capacity.
    """
    
    def __init__(self, capacity: int, bucket_size: int = 4, max_kicks: int = 500) -> None:
        """
        Initialize the Cuckoo filter.
        
        Args:
            capacity: Number of items the filter is expected to hold
            bucket_size: Number of entries per bucket (default: 4)
            max_kicks: Maximum number of displacement attempts (default: 500)
            
        Time Complexity: O(capacity) for initialization
        Space Complexity: O(capacity * bucket_size)
        """
        self.capacity = capacity
        self.bucket_size = bucket_size
        self.max_kicks = max_kicks
        self.tables: List[List[Optional[int]]] = [[None] * self.bucket_size for _ in range(2 * capacity)]
        self.fingerprint_size = 8  # bits
    
    def _my_hash(self, item: Any, i: int) -> int:
        """
        Generate hash for an item.
        
        Args:
            item: Item to hash
            i: Index of hash function (0 or 1)
            
        Returns:
            int: Hash value
        """
        s = str(item) + str(i)
        return int(hashlib.sha256(s.encode()).hexdigest(), 16) % (2 * self.capacity)
    
    def _fingerprint(self, item: Any) -> int:
        """
        Generate fingerprint for an item.
        
        Args:
            item: Item to generate fingerprint for
            
        Returns:
            int: Fingerprint value
        """
        s = str(item)
        return int(hashlib.sha256(s.encode()).hexdigest(), 16) % (2 ** self.fingerprint_size)
    
    def insert(self, item: Any) -> bool:
        """
        Insert an item into the filter.
        
        Args:
            item: Item to insert
            
        Returns:
            bool: True if insertion successful, False if filter is too full
            
        Time Complexity: O(1) amortized
        """
        fp = self._fingerprint(item)
        pos1 = self._my_hash(item, 0)
        pos2 = self._my_hash(item, 1)
        
        if self._insert_into_bucket(fp, pos1):
            return True
        if self._insert_into_bucket(fp, pos2):
            return True
        
        current_fp = fp
        current_pos = pos1
        for _ in range(self.max_kicks):
            bucket = self.tables[current_pos]
            for i in range(self.bucket_size):
                if bucket[i] is not None:
                    next_fp = bucket[i]
                    bucket[i] = current_fp
                    current_fp = next_fp
                    break
            
            if current_pos == pos1:
                current_pos = pos2
            else:
                current_pos = pos1
            
            if self._insert_into_bucket(current_fp, current_pos):
                return True
        
        return False
    
    def _insert_into_bucket(self, fp: int, pos: int) -> bool:
        """
        Try to insert a fingerprint into a bucket.
        
        Args:
            fp: Fingerprint to insert
            pos: Position of bucket
            
        Returns:
            bool: True if insertion successful, False if bucket is full
        """
        bucket = self.tables[pos]
        for i in range(self.bucket_size):
            if bucket[i] is None:
                bucket[i] = fp
                return True
        return False
    
    def search(self, target: Any) -> int:
        """
        Search for a target item in the filter.
        
        Args:
            target: Item to search for
            
        Returns:
            int: 1 if the item might be in the set, -1 if definitely not in the set
            
        Time Complexity: O(1)
        """
        return 1 if target in self else -1
    
    def __contains__(self, item: Any) -> bool:
        """
        Check if an item might be in the filter.
        
        Args:
            item: Item to check
            
        Returns:
            bool: True if item might be in set, False if definitely not in set
            
        Time Complexity: O(1)
        """
        fp = self._fingerprint(item)
        pos1 = self._my_hash(item, 0)
        pos2 = self._my_hash(item, 1)
        
        bucket1 = self.tables[pos1]
        bucket2 = self.tables[pos2]
        
        if bucket1 is not None:
            for i in range(self.bucket_size):
                if bucket1[i] == fp:
                    return True
        if bucket2 is not None:
            for i in range(self.bucket_size):
                if bucket2[i] == fp:
                    return True
        
        return False
    
    def delete(self, item: Any) -> bool:
        """
        Delete an item from the filter.
        
        Args:
            item: Item to delete
            
        Returns:
            bool: True if item was found and deleted, False otherwise
            
        Time Complexity: O(1)
        """
        fp = self._fingerprint(item)
        pos1 = self._my_hash(item, 0)
        pos2 = self._my_hash(item, 1)
        
        bucket1 = self.tables[pos1]
        bucket2 = self.tables[pos2]
        
        if bucket1 is not None:
            for i in range(self.bucket_size):
                if bucket1[i] == fp:
                    bucket1[i] = None
                    return True
        if bucket2 is not None:
            for i in range(self.bucket_size):
                if bucket2[i] == fp:
                    bucket2[i] = None
                    return True
        
        return False
