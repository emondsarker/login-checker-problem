import sys
import os
import random
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.bloom_filter import BloomFilter
from plotter import Plotter
from dataset.dataset_constants import DATASET_LIMIT, DATASET_STEP

n_values = []
runtime_values = []

for i in range(DATASET_STEP, DATASET_LIMIT, DATASET_STEP):
    with open('dataset.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]

        dataset = lines[:i]
        if(len(dataset) == 0):
            raise Exception("Dataset is empty.")
        
        filter = BloomFilter(dataset)
        
        times = []
        for _ in range(10):
            target = dataset[random.randint(0, len(dataset) - 1)]
            start_time = time.time()
            result = filter.search(target)
            end_time = time.time()
            run_time = end_time - start_time
            times.append(run_time)        
        
        run_time = sum(times) / len(times)
        n_values.append(len(dataset))
        runtime_values.append(run_time)
        
        print(f"Test Bloom Filter: n={len(dataset)}, target={target}, result={result}, runtime={run_time:.6f}s")

plotter = Plotter('runtime_analysis')
plotter.generate_line_graph(
    'N / Number of Login Names', 
    n_values, 
    'Runtime value / seconds',
    runtime_values, 
    'bloom_filter'
)

# Save the n values and runtime values to a file

with open('bloom_filter_runtime_data.txt', 'w') as file:
    for n, runtime in zip(n_values, runtime_values):
        file.write(f"{n},{runtime}\n")