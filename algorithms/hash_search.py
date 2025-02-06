def hash_search(arr, target):
    hash_table = {item: index for index, item in enumerate(arr)}
    return hash_table.get(target, -1)
