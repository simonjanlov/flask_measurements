import matplotlib
matplotlib.use('Agg')  # Set the backend to use Agg
import matplotlib.pyplot as plt
import pandas as pd
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

    # Exclude leading or trailing 0-values from the plot
    first_value_index = 0
    
    if 0 in weights:
        while weights[first_value_index] == 0:
            first_value_index += 1

        while weights[-1] == 0:
            weights.pop()

    truncated_weights = weights[first_value_index:]
    truncated_weeks = weeks[first_value_index:first_value_index + len(truncated_weights)]


    # Clean up 0 values in the middle of the data using linear interpolation
    df = pd.DataFrame({'weeks':truncated_weeks, 'weights':truncated_weights})
    df.set_index('weeks', inplace=True)
    df.replace(0, np.nan, inplace=True)
    df['weights'] = df['weights'].interpolate(method='linear')

    # Create plot and save to .png file
    plt.plot(df.index, df.weights)
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
    plt.close()
    


if __name__=="__main__":
    weight_data = [0.0, 0.0, 63.5, 63.3, 62.0, 0.0, 65.0, 65.5, 63.0, 0.0, 0.0]
    generate_weight_graph(weight_data)
