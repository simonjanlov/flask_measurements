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
    
    # Saving the graph to a file
    plt.savefig(os.path.join('app', 'static', 'img', 'graph.png')) # Save the graph as a static file

    # Alternatively, you could return the binary data
    # and serve it directly without saving to a file
    # import io
    # buf = io.BytesIO()
    # plt.savefig(buf, format='png')
    # buf.seek(0)
    # return buf.getvalue()

    plt.close()