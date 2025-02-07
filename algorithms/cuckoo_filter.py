def cuckoo_filter(arr, target):
    table_size = len(arr) * 2
    max_kicks = 500
    table1 = [None] * table_size
    table2 = [None] * table_size
    
    def hash1(item):
        return hash(item) % table_size
    
    def hash2(item):
        return hash(item * 2) % table_size
    
    for i, item in enumerate(arr):
        pos1 = hash1(item)
        pos2 = hash2(item)
        
        if table1[pos1] is None:
            table1[pos1] = (item, i)
            continue
            
        if table2[pos2] is None:
            table2[pos2] = (item, i)
            continue
            
        current = (item, i)
        current_table = 1
        
        success = False
        for _ in range(max_kicks):
            if current_table == 1:
                current, table1[pos1] = table1[pos1], current
                if current is None:
                    success = True
                    break
                current_table = 2
                pos2 = hash2(current[0])
            else:
                current, table2[pos2] = table2[pos2], current
                if current is None:
                    success = True
                    break
                current_table = 1
                pos1 = hash1(current[0])
        
        if not success:
            for j in range(table_size):
                if table1[j] is None:
                    table1[j] = (item, i)
                    break
                if table2[j] is None:
                    table2[j] = (item, i)
                    break
    
    pos1, pos2 = hash1(target), hash2(target)
    if table1[pos1] and table1[pos1][0] == target:
        return table1[pos1][1]
    if table2[pos2] and table2[pos2][0] == target:
        return table2[pos2][1]
    return -1
