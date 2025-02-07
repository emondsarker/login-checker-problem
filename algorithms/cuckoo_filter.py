import hashlib

class CuckooFilter:
    def __init__(self, capacity, bucket_size=4, max_kicks=500):
        self.capacity = capacity
        self.bucket_size = bucket_size 
        self.max_kicks = max_kicks
        self.tables = [[None] * self.bucket_size for _ in range(2 * capacity)]
        self.fingerprint_size = 8  

    def _my_hash(self, item, i):
        s = str(item) + str(i)
        return int(hashlib.sha256(s.encode()).hexdigest(), 16) % (2*self.capacity)

    def _fingerprint(self, item):
        s = str(item)
        return int(hashlib.sha256(s.encode()).hexdigest(), 16) % (2**self.fingerprint_size)

    def insert(self, item):
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

    def _insert_into_bucket(self, fp, pos):
        bucket = self.tables[pos]
        for i in range(self.bucket_size):
            if bucket[i] is None:
                bucket[i] = fp
                return True
        return False

    def __contains__(self, item):
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

    def delete(self, item):
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
