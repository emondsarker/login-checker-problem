import os
import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, plot_directory='plots'):
        self.plot_directory = plot_directory
        if not os.path.exists(self.plot_directory):
            os.makedirs(self.plot_directory)
            
    def generate_line_graph(self, x_label: str, n_values: list, y_value: str, runtime_values: list, file_name: str):
        plt.plot(n_values, runtime_values, marker='o', color='b')
        plt.xlabel(x_label)
        plt.ylabel('Runtime (s)')
        plt.title(f'{file_name} - Runtime Analysis')
        plt.grid()
        plt.savefig(f'{self.plot_directory}/{file_name}.png')
        plt.close()
        
        
        