import matplotlib.pyplot as plt
import numpy as np

def plot_spider_graph(labels, values):
    # Number of variables/values
    num_vars = len(labels)
    
    # Calculate angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # Repeat the first angle to close the circle
    
    # Make a polar plot
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
    
    # Plot data
    values += values[:1]  # Repeat the first value to close the circle
    ax.plot(angles, values, linewidth=1, linestyle='solid', marker='o')
    
    # Fill the area inside the plot
    ax.fill(angles, values, alpha=0.25)
    
    # Set labels for each axis
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    # Set the title
    ax.set_title('Spider Graph')

    # Display the plot
    plt.show()

# Example usage:
labels = ['Parameter 1', 'Parameter 2', 'Parameter 3', 'Parameter 4', 'Parameter 5']
values = [0.7, 0.9, 0.5, 0.8, 0.6]

plot_spider_graph(labels, values)