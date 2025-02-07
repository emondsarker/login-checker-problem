# Login Checker Algorithm Comparison

This project compares different algorithms for checking user login credentials, analyzing their performance characteristics and runtime efficiency. It implements and compares the following algorithms:

- Binary Search
- Bloom Filter
- Cuckoo Filter
- Hash Search
- Linear Search

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup Instructions

1. Clone the repository:

```bash
git clone <repository-url>
cd login-checker-problem
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Running Instructions

### 1. Generate Dataset

First, generate the dataset of usernames that will be used for testing. You can generate either a sorted or unsorted dataset:

For unsorted dataset:

```bash
python dataset/generate_dataset.py
```

For sorted dataset (required for binary search):

```bash
python dataset/generate_dataset.py --sorted
```

This will generate a dataset with 1 million usernames. If you want to change the total amount of usernames, modify the file `dataset_constants.py`

### 2. Run Tests

Individual algorithm tests can be run from the tests directory:

```bash
# Run binary search test
python tests/binary_search.py

# Run bloom filter test
python tests/bloom_filter.py

# Run cuckoo filter test
python tests/cuckoo_filter.py

# Run hash search test
python tests/hash_search.py

# Run linear search test
python tests/linear_search.py
```

### 3. Generate Performance Plots

The project includes plotting capabilities to visualize the performance characteristics of each algorithm. Run the plotting scripts:

```bash
# Generate plots for each algorithm
python plotter/plot_binary_search.py
python plotter/plot_bloom_filter.py
python plotter/plot_cuckoo_filter.py
python plotter/plot_hash_search.py
python plotter/plot_linear_search.py
```

Generated plots will be saved in the `runtime_analysis/` directory.

## Project Structure

- `algorithms/`: Contains implementations of different search algorithms
- `dataset/`: Contains dataset generation scripts and constants
- `plots/`: Directory for storing generated plots
- `plotter/`: Contains plotting scripts for performance visualization
- `runtime_analysis/`: Contains generated performance analysis plots
- `tests/`: Contains test files for each algorithm

## Performance Analysis

The runtime analysis plots for each algorithm can be found in the `runtime_analysis/` directory:

- `binary_search.png`
- `bloom_filter.png`
- `cuckoo_filter.png`
- `hash_search.png`
- `linear_search.png`

These plots provide visual comparisons of the algorithms' performance characteristics across different dataset sizes.
