import matplotlib
matplotlib.use('Agg')  # Set the backend to use Agg
import matplotlib.pyplot as plt
import numpy as np
import os

def generate_graph():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.plot(x, y)
    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')
    plt.title('Example Matplotlib Graph')
    
    # Save the graph to a file
    plt.savefig(os.path.join('app', 'static', 'img', 'graph.png'))

    # Alternatively, you could return the binary data
    # and serve it directly without saving to a file
    # import io
    # buf = io.BytesIO()
    # plt.savefig(buf, format='png')
    # buf.seek(0)
    # return buf.getvalue()

    plt.close()

def generate_weight_graph(weight_data):
    x_values = list(range(len(weight_data)))
    y_values = weight_data
    name = "User"

    plt.plot(x_values, y_values)
    custom_labels = ['Starting point',
                    'Week 1', 
                    'Week 2', 
                    'Week 3', 
                    'Week 4',
                    'Week 5', 
                    'Week 6', 
                    'Week 7', 
                    'Week 8',
                    'Week 9', 
                    'Week 10']
    plt.xticks(x_values, custom_labels, rotation=30, ha='right', rotation_mode='anchor') # tweak this to that the labels fit (45 degrees tilt?)
    plt.xlabel('')
    plt.ylabel('Weight(Kg)')
    plt.title(f"{name}'s Weight Progress")
    plt.tight_layout()

    # Save the graph to a file
    plt.savefig(os.path.join('app', 'static', 'img', 'user_graph.png'))
    


if __name__=="__main__":
    weight_data = [66.0, 65.0, 65.5, 65.3, 64.8, 64.0, 64.0, 63.5, 63.0, 63.0, 62.0]
    generate_weight_graph(weight_data)
