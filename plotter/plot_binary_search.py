import sys
import os
import random
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.binary_search import BinarySearch
from plotter import Plotter
from dataset.dataset_constants import DATASET_LIMIT, DATASET_STEP

n_values = []
runtime_values = []

for i in range(DATASET_STEP, DATASET_LIMIT, DATASET_STEP):
    with open('dataset.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        dataset = sorted(lines[:i])  # Sort the dataset for binary search
        binary_search = BinarySearch(dataset).search
        if(len(dataset) == 0):
            raise Exception("Dataset is empty.")
        
        times = []
        for _ in range(100):
            target = dataset[random.randint(0, len(dataset) - 1)]
            start_time = time.time()
            result = binary_search(target)
            end_time = time.time()
            run_time = end_time - start_time
            if result == -1:
                raise Exception(f"Element {target} not found in dataset.")
            times.append(run_time)        
        
        run_time = sum(times) / len(times)
        n_values.append(len(dataset))
        runtime_values.append(run_time)
        
        print(f"Test Binary Search: n={len(dataset)}, target={target}, result={result}, runtime={run_time:.6f}s")

plotter = Plotter('runtime_analysis')
plotter.generate_line_graph(
    'N / Number of Login Names', 
    n_values, 
    'Average Runtime / seconds',
    runtime_values, 
    'Binary Search Runtime Analysis'
)

# save the n values and runtime values to a file

with open('binary_search_runtime_data.txt', 'w') as file:
    for n, runtime in zip(n_values, runtime_values):
        file.write(f"{n},{runtime}\n")