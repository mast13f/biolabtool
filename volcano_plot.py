
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# volcano plot


# user input
x = input('x:')
y = input('y:')
name = input('name:')
fc_threshold_lower = float(input('fc_threshold_lower:'))
fc_threshold_upper = float(input('fc_threshold_upper:'))
sig_threshold = float(input('sig_threshold:'))

def volcano_plot(data, x, y, name, fc_threshold_lower, fc_threshold_upper, sig_threshold):
    x_axis = x
    y_axis = y
    threshold = sig_threshold
    fc_threshold_lower = fc_threshold_lower
    fc_threshold_upper = fc_threshold_upper

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