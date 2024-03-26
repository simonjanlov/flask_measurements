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
    weeks = list(range(len(weight_data)))
    weights = weight_data
    name = "User"

    # TO DO - clean up 0 values in the middle
    # TO DO - edit the following logic to work also for the opposite scenario, where the beginning contains only 0's

    # Find the last week with a non-zero weight value
    if 0 in weights:
        index_of_first_zero = weights.index(0)
        if all(weight == 0 for weight in weights[index_of_first_zero:]):
            last_non_zero_week = weeks[index_of_first_zero - 1]
        else:
            last_non_zero_week = weeks[-1]
    else:
        last_non_zero_week = weeks[-1]

    # Truncate the data
    truncated_weeks = weeks[:last_non_zero_week + 1]
    truncated_weights = weights[:last_non_zero_week + 1]

    plt.plot(truncated_weeks, truncated_weights)
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
    plt.xlim(-0.5, len(weeks) -0.5) # Sets the x-axis limits to ensure it extends to all 11 weeks
    plt.xticks(weeks, custom_labels, rotation=30, ha='right', rotation_mode='anchor')
    plt.xlabel('')
    plt.ylabel('Weight(Kg)')
    plt.title(f"{name}'s Weight Progress")
    plt.tight_layout()

    # Save the graph to a file
    plt.savefig(os.path.join('app', 'static', 'img', 'user_graph.png'))
    


if __name__=="__main__":
    weight_data = [66.0, 65.0, 65.5, 65.3, 64.8, 64.0, 65.0, 63.5, 63.0, 0.0, 0.0]
    generate_weight_graph(weight_data)
