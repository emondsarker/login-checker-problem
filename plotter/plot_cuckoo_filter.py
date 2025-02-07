import sys
import os
import random
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.cuckoo_filter import CuckooFilter
from plotter import Plotter
from dataset.dataset_constants import DATASET_LIMIT, DATASET_STEP

n_values = []
runtime_values = []

for i in range(DATASET_STEP, DATASET_LIMIT, DATASET_STEP):
    with open('dataset.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print(i)
        dataset = lines[:i]
        if(len(dataset) == 0):
            raise Exception("Dataset is empty.")
        
        # Create a new filter for each dataset size
        cuckoo_filter = CuckooFilter(capacity=len(dataset))
        
        # Insert all items first
        for item in dataset:
            cuckoo_filter.insert(item)
        
        times = []
        for _ in range(10):
            # Test lookup performance
            target = dataset[random.randint(0, len(dataset) - 1)]
            start_time = time.time()
            result = target in cuckoo_filter  # Using membership testing
            end_time = time.time()
            run_time = end_time - start_time
            times.append(run_time)        
        
        run_time = sum(times) / len(times)
        n_values.append(len(dataset))
        runtime_values.append(run_time)
        
        print(f"Test Cuckoo Filter: n={len(dataset)}, target={target}, found={result}, runtime={run_time:.6f}s")

plotter = Plotter('runtime_analysis')
plotter.generate_line_graph(
    'N / Number of Login Names', 
    n_values, 
    'Runtime value / seconds',
    runtime_values, 
    'cuckoo_filter'
)
