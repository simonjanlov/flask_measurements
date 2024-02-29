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

    plt.plot(x_values, y_values)
    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')
    plt.title('Example Matplotlib Graph')

    # Save the graph to a file
    plt.savefig(os.path.join('app', 'static', 'img', 'user_graph.png'))

    


if __name__=="__main__":
    weight_data = [3.0, 4.0, 5.0, 6.0, 5.0, 4.0, 5.0, 6.0, 4.0, 6.0, 5.0]
    generate_weight_graph(weight_data)
