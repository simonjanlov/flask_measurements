import matplotlib
matplotlib.use('Agg')  # Set the backend to use Agg
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import matplotlib.animation as animation
import subprocess
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
    ytick_labels = ['{:.1f}'.format(val) for val in plt.yticks()[0]]
    plt.yticks(plt.yticks()[0], ytick_labels)
    plt.xlabel('')
    plt.ylabel('Weight(Kg)')
    plt.title(f"{name}'s Weight Progress")
    plt.tight_layout()

    # Save the graph to a file
    plt.savefig(os.path.join('app', 'static', 'img', 'user_graph.png'))
    plt.close()
    

def add_list_grain(weight_list, week_list, divisions_per_value):

    i = 0

    for _ in range(len(weight_list) - 1):
        first_weight_val = weight_list[i]
        second_weight_val = weight_list[i+1]
        current_weight_val = first_weight_val
        weight_step = (second_weight_val - first_weight_val) / divisions_per_value

        first_week_val = week_list[i]
        second_week_val = week_list[i+1]
        current_week_val = first_week_val
        week_step = (second_week_val - first_week_val) / divisions_per_value

        for _ in range(divisions_per_value - 1):
            i += 1
            
            current_weight_val += weight_step
            current_week_val += week_step
            weight_list.insert(i, round(current_weight_val,2))
            week_list.insert(i, round(current_week_val, 2))
        i += 1

    return weight_list, week_list


def exclude_leading_and_trailing_0s(list_of_values: list):

    first_value_index = 0
    
    if 0 in list_of_values:
        while list_of_values[first_value_index] == 0:
            first_value_index += 1

        while list_of_values[-1] == 0:
            list_of_values.pop()
    
    return list_of_values, first_value_index


def generate_weight_graph_gif(weight_data):
    weeks = list(range(len(weight_data)))
    weights = weight_data
    name = "User"

    # Exclude leading or trailing 0-values from the plot
    weights, first_weight_value_index = exclude_leading_and_trailing_0s(weights)

    truncated_weights = weights[first_weight_value_index:]
    truncated_weeks = weeks[first_weight_value_index:first_weight_value_index + len(truncated_weights)]

    # Clean up 0 values in the middle of the data using linear interpolation
    df = pd.DataFrame({'weeks':truncated_weeks, 'weights':truncated_weights})
    df.set_index('weeks', inplace=True)
    df.replace(0, np.nan, inplace=True)
    df['weights'] = df['weights'].interpolate(method='linear')

    plot_weights, plot_weeks = add_list_grain(list(df.weights), list(df.index), divisions_per_value=10)

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
    
    metadata = dict(title="Movie", artist="SimonJ")
    writer = PillowWriter(fps=15, metadata=metadata)

    fig = plt.figure()
    l, = plt.plot([],[])
    plt.xlim(-0.5, len(weeks) -0.5) # Sets the x-axis limits to ensure it extends to all 11 weeks
    plt.ylim(min(plot_weights)-2, max(plot_weights)+2)
    plt.xticks(weeks, custom_labels, rotation=30, ha='right', rotation_mode='anchor')
    ytick_labels = ['{:.1f}'.format(val) for val in plt.yticks()[0]]
    plt.yticks(plt.yticks()[0], ytick_labels)
    plt.xlabel('')
    plt.ylabel('Weight(Kg)')
    plt.title(f"{name}'s Weight Progress")
    plt.tight_layout()

    gif_path = os.path.join('app', 'static', 'img', 'user_graph.gif')

    with writer.saving(fig, gif_path, 100): # 100 is DPI of the image
        for i in range(len(plot_weeks)):
            l.set_data(plot_weeks[:i], plot_weights[:i])
            writer.grab_frame()

    plt.close()


if __name__=="__main__":
    weight_data = [0.0, 0.0, 63.5, 63.3, 63.1, 0.0, 64.0, 63.2, 63.0, 0.0, 0.0]
    generate_weight_graph_gif(weight_data)
