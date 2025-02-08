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

## Dependencies

The project uses the following main dependencies:

- matplotlib: For plotting performance graphs
- numpy: For numerical computations
- pandas: For data manipulation and analysis
- Faker: For generating test usernames
- Additional dependencies are listed in requirements.txt

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

## Dataset Configuration

The dataset size can be configured by modifying `dataset/dataset_constants.py`. The default configuration generates:

- Total usernames: 1 million (DATASET_LIMIT)
- Step size for performance testing: Configurable via DATASET_STEP

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

The project includes several plotting capabilities to visualize the performance characteristics of each algorithm:

#### Individual Algorithm Plots

Generate performance plots for each algorithm separately:

```bash
# Generate plots for each algorithm
python plotter/plot_binary_search.py
python plotter/plot_bloom_filter.py
python plotter/plot_cuckoo_filter.py
python plotter/plot_hash_search.py
python plotter/plot_linear_search.py
```

#### Comparison Plots

Generate plots comparing all algorithms:

```bash
# Generate standard comparison plot
python plotter/plot_comparison.py

# Generate logarithmic scale comparison plot
python plotter/plot_log_comparison.py
```

The comparison plots provide two different views:

- `algorithm_comparison.png`: Standard scale comparison of all algorithms
- `algorithm_comparison_log10.png`: Logarithmic scale comparison for better visualization of performance differences

All generated plots will be saved in the `runtime_analysis/` directory.

## Project Structure

- `algorithms/`: Contains implementations of different search algorithms
- `dataset/`: Contains dataset generation scripts and constants
- `plots/`: Directory for storing generated plots
- `plotter/`: Contains plotting scripts for performance visualization
  - Individual algorithm plotting scripts
  - Comparison plotting scripts (standard and logarithmic scales)
- `runtime_analysis/`: Contains generated performance analysis plots and CSV data
  - Individual algorithm performance plots
  - Algorithm comparison plots
  - Raw performance data in CSV format
- `tests/`: Contains test files for each algorithm

## Performance Analysis

The runtime analysis plots for each algorithm can be found in the `runtime_analysis/` directory:

- Individual algorithm plots:

  - `binary_search.png`
  - `bloom_filter.png`
  - `cuckoo_filter.png`
  - `hash_search.png`
  - `linear_search.png`

- Comparison plots:
  - `algorithm_comparison.png`: Standard scale comparison
  - `algorithm_comparison_log10.png`: Logarithmic scale comparison
  - `algorithm_comparison.csv`: Raw performance data

These plots provide visual comparisons of the algorithms' performance characteristics across different dataset sizes. The logarithmic scale plot (`algorithm_comparison_log10.png`) is particularly useful for visualizing performance differences when the runtime variations between algorithms are large.
