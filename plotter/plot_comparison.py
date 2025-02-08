import sys
import os
import random
import time
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.binary_search import BinarySearch
from algorithms.hash_search import HashSearch
from algorithms.linear_search import LinearSearch
from algorithms.bloom_filter import BloomFilter
from algorithms.cuckoo_filter import CuckooFilter
from dataset.dataset_constants import DATASET_LIMIT, DATASET_STEP

# Data structures to store results for each algorithm
binary_n_values = []
binary_runtime_values = []
hash_n_values = []
hash_runtime_values = []
linear_n_values = []
linear_runtime_values = []
bloom_n_values = []
bloom_runtime_values = []
cuckoo_n_values = []
cuckoo_runtime_values = []

REPEAT_FOR = 10

# Collect Linear Search data
print("\nCollecting Linear Search data...")
for i in range(DATASET_STEP, DATASET_LIMIT, DATASET_STEP):
    with open('dataset.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        dataset = lines[:i]
        linear_search = LinearSearch(dataset).search
        
        times = []
        for _ in range(REPEAT_FOR):
            target = dataset[random.randint(0, len(dataset) - 1)]
            start_time = time.time()
            result = linear_search(target)
            end_time = time.time()
            run_time = end_time - start_time
            if result == -1:
                raise Exception(f"Element {target} not found in dataset.")
            times.append(run_time)
        
        run_time = sum(times) / len(times)
        linear_n_values.append(len(dataset))
        linear_runtime_values.append(run_time)
        print(f"Linear Search: n={len(dataset)}, runtime={run_time:.6f}s")

# Collect Binary Search data
print("\nCollecting Binary Search data...")
for i in range(DATASET_STEP, DATASET_LIMIT, DATASET_STEP):
    with open('dataset.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        dataset = sorted(lines[:i])  # Sort for binary search
        binary_search = BinarySearch(dataset).search
        
        times = []
        for _ in range(REPEAT_FOR):
            target = dataset[random.randint(0, len(dataset) - 1)]
            start_time = time.time()
            result = binary_search(target)
            end_time = time.time()
            run_time = end_time - start_time
            if result == -1:
                raise Exception(f"Element {target} not found in dataset.")
            times.append(run_time)
        
        run_time = sum(times) / len(times)
        binary_n_values.append(len(dataset))
        binary_runtime_values.append(run_time)
        print(f"Binary Search: n={len(dataset)}, runtime={run_time:.6f}s")

# Collect Hash Search data
print("\nCollecting Hash Search data...")
for i in range(DATASET_STEP, DATASET_LIMIT, DATASET_STEP):
    with open('dataset.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        dataset = lines[:i]
        hash_search = HashSearch(dataset).search
        
        times = []
        for _ in range(REPEAT_FOR):
            target = dataset[random.randint(0, len(dataset) - 1)]
            start_time = time.time()
            result = hash_search(target)
            end_time = time.time()
            run_time = end_time - start_time
            if result == -1:
                raise Exception(f"Element {target} not found in dataset.")
            times.append(run_time)
        
        run_time = sum(times) / len(times)
        hash_n_values.append(len(dataset))
        hash_runtime_values.append(run_time)
        print(f"Hash Search: n={len(dataset)}, runtime={run_time:.6f}s")

# Collect Bloom Filter data
print("\nCollecting Bloom Filter data...")
for i in range(DATASET_STEP, DATASET_LIMIT, DATASET_STEP):
    with open('dataset.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        dataset = lines[:i]
        bloom_filter = BloomFilter(dataset)
        
        times = []
        for _ in range(REPEAT_FOR):
            target = dataset[random.randint(0, len(dataset) - 1)]

            # Create and populate filter
            for item in dataset:
                bloom_filter._add(item)
            
            start_time = time.time()
            result = bloom_filter.search(target)
            end_time = time.time()
            run_time = end_time - start_time
            times.append(run_time)
        
        run_time = sum(times) / len(times)
        bloom_n_values.append(len(dataset))
        bloom_runtime_values.append(run_time)
        print(f"Bloom Filter: n={len(dataset)}, runtime={run_time:.6f}s")

# Collect Cuckoo Filter data
print("\nCollecting Cuckoo Filter data...")
for i in range(DATASET_STEP, DATASET_LIMIT, DATASET_STEP):
    with open('dataset.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        dataset = lines[:i]
        cuckoo_filter = CuckooFilter(capacity=len(dataset))
        # Create and populate filter
        insert_failed = False
        for item in dataset:
            if not cuckoo_filter.insert(item):
                print(f"Warning: Cuckoo filter failed to insert item at size {len(dataset)}")
                insert_failed = True
                break
            
        times = []
        for _ in range(REPEAT_FOR):
            target = dataset[random.randint(0, len(dataset) - 1)]
            start_time = time.time()
            result = cuckoo_filter.search(target)
            end_time = time.time()
            run_time = end_time - start_time
            times.append(run_time)
        
        if times:
            run_time = sum(times) / len(times)
            cuckoo_n_values.append(len(dataset))
            cuckoo_runtime_values.append(run_time)
            print(f"Cuckoo Filter: n={len(dataset)}, runtime={run_time:.6f}s")


# Store all results in a CSV file (for easier visualization and comparison)
with open('runtime_analysis/algorithm_comparison.csv', 'w') as file:
    file.write('n,linear,binary,hash,bloom,cuckoo\n')
    for i in range(len(linear_n_values)):
        file.write(f"{linear_n_values[i]},{linear_runtime_values[i]},{binary_runtime_values[i]},{hash_runtime_values[i]},{bloom_runtime_values[i]},{cuckoo_runtime_values[i]}\n")


# Plot all results
plt.figure(figsize=(12, 8))

plt.plot(linear_n_values, linear_runtime_values, marker='o', color='g', label='Linear Search')
plt.plot(binary_n_values, binary_runtime_values, marker='o', color='b', label='Binary Search')
plt.plot(hash_n_values, hash_runtime_values, marker='o', color='r', label='Hash Search')
plt.plot(bloom_n_values, bloom_runtime_values, marker='o', color='purple', label='Bloom Filter')
plt.plot(cuckoo_n_values, cuckoo_runtime_values, marker='o', color='orange', label='Cuckoo Filter')

plt.xlabel('N / Number of Login Names')
plt.ylabel('Runtime (s)')
plt.title('Algorithm Runtime Comparison')
plt.grid(True)
plt.legend()

# Save the plot
if not os.path.exists('runtime_analysis'):
    os.makedirs('runtime_analysis')
plt.savefig('runtime_analysis/algorithm_comparison.png')
plt.close()
