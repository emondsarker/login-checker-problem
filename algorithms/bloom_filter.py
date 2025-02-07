class BloomFilter:
    def __init__(self, arr):
        self.size = len(arr) * 10
        self.bit_array = [0] * self.size
        
        for item in arr:
            self._add(item)
    
    def _hash1(self, item):
        return hash(item) % self.size
    
    def _hash2(self, item):
        return hash(item * 2) % self.size
    
    def _hash3(self, item):
        return hash(item * 3) % self.size
    
    def _add(self, item):
        self.bit_array[self._hash1(item)] = 1
        self.bit_array[self._hash2(item)] = 1
        self.bit_array[self._hash3(item)] = 1
    
    def search(self, target):
        if (self.bit_array[self._hash1(target)] and 
            self.bit_array[self._hash2(target)] and 
            self.bit_array[self._hash3(target)]):
            return 1
        return -1

def bloom_filter(arr, target):
    filter = BloomFilter(arr)
    return filter.search(target)
