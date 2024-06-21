import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ask user to input the file path
def get_file_path():
    file_path = input("Please enter the file path: ")
    return file_path

# read the file
def read_file(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")
        return None
    except Exception as e:
        print("An error occurred. Please try again.")
        return None
    
# display the columns of the data
def display_columns(data):
    print("The columns in the data are: ")
    for column in data.columns:
        print(column)


# pick the graph type to plot: volcano plot, MA plot, PCA plot, heatmap
def pick_graph_type():
    print("Please pick the graph type you would like to plot: ")
    print("1. Volcano plot")
    print("2. MA plot")
    print("3. PCA plot")
    print("4. Heatmap")
    graph_type = input("Enter the number of the graph type you would like to plot: ")
    return graph_type

# volcano plot
def volcano_plot(data):
    x_axis = input("Enter the column name for X axis: ")
    y_axis = input("Enter the column name for Y axis: ")
    threshold = float(input("Enter the threshold value: "))
    
    plt.scatter(x=data[x_axis], y=data[y_axis], s=1, label="Not significant")

    # highlight down- or up- regulated genes
    down = data[(data[x_axis] <= -threshold) & (data[y_axis] >= threshold)]
    up = data[(data[x_axis] >= threshold) & (data[y_axis] >= threshold)]

    plt.scatter(x=down[x_axis], y=down[y_axis], s=3, label="Down-regulated", color="blue")
    plt.scatter(x=up[x_axis], y=up[y_axis], s=3, label="Up-regulated", color="red")

    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.axvline(-threshold, color="grey", linestyle="--")
    plt.axvline(threshold, color="grey", linestyle="--")
    plt.axhline(threshold, color="grey", linestyle="--")
    plt.legend()
    plt.show()



# main function

df = pd.read_csv('test.csv')
volcano_plot(df)