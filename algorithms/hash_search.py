class HashSearch:
    def __init__(self, arr):
        self.hash_table = {item: index for index, item in enumerate(arr)}
    
    def search(self, target):
        return self.hash_table.get(target, -1)

def hash_search(arr, target):
    searcher = HashSearch(arr)
    return searcher.search(target)
