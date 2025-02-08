import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Read the CSV file
df = pd.read_csv('runtime_analysis/algorithm_comparison.csv')

# Create the plot
plt.figure(figsize=(12, 8))

# Plot each algorithm with natural log of runtime values
plt.plot(df['n'], np.log10(df['linear']), marker='o', color='g', label='Linear Search', linewidth=2)
plt.plot(df['n'], np.log10(df['binary']), marker='o', color='b', label='Binary Search', linewidth=2)
plt.plot(df['n'], np.log10(df['hash']), marker='o', color='r', label='Hash Search', linewidth=2)
plt.plot(df['n'], np.log10(df['bloom']), marker='o', color='purple', label='Bloom Filter', linewidth=2)
plt.plot(df['n'], np.log10(df['cuckoo']), marker='o', color='orange', label='Cuckoo Filter', linewidth=2)

plt.xlabel('N (Number of Login Names)', fontsize=12)
plt.ylabel('ln(Runtime) in seconds', fontsize=12)
plt.title('Algorithm Runtime Comparison (Natural Log Scale)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=10)

# Customize the plot
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
if not os.path.exists('runtime_analysis'):
    os.makedirs('runtime_analysis')
plt.savefig('runtime_analysis/algorithm_comparison_log10.png', dpi=300, bbox_inches='tight')
plt.close()
