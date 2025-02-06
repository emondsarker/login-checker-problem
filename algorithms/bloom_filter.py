def bloom_filter(arr, target):
    bit_array = [0] * (len(arr) * 10)
    
    def hash1(item):
        return hash(item) % len(bit_array)
    
    def hash2(item):
        return hash(item * 2) % len(bit_array)
    
    def hash3(item):
        return hash(item * 3) % len(bit_array)
    
    for i, item in enumerate(arr):
        bit_array[hash1(item)] = 1
        bit_array[hash2(item)] = 1
        bit_array[hash3(item)] = 1
        
    if bit_array[hash1(target)] and bit_array[hash2(target)] and bit_array[hash3(target)]:
        for i, item in enumerate(arr):
            if item == target:
                return i
    return -1
