import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from adjustText import adjust_text

def get_user_input():
    # User input - for testing only, replace with actual user input as needed
    x = 'Log2FC'
    y = 'minuslog10(pval)'
    name = 'Name'
    fc_threshold_lower = -0.5
    fc_threshold_upper = 0.5
    sig_threshold = 0.5
    show_labels = False
    ns_color = 'lightgrey'
    ur_color = 'deepskyblue'
    dr_color = 'orangered'
    mark_all = False
    
    # Points of interest input
    pofi_input = input('Points of interest? (y/n):')
    if pofi_input == 'y':
        pofi = input('Enter the name of points of interest (comma separated):').split(',')
    else:
        pofi = []
    
    return (x, y, name, fc_threshold_lower, fc_threshold_upper, sig_threshold, show_labels, ns_color, ur_color, dr_color, mark_all, pofi)

def check_pofi_in_data(pofi, data, name):
    valid_pofi = []
    for p in pofi:
        if p in data[name].values:
            valid_pofi.append(p)
        else:
            print(f'{p} not found in the data')
    return valid_pofi

def plot_volcano(data, x, y, name, fc_threshold_lower, fc_threshold_upper, sig_threshold, show_labels, ns_color, ur_color, dr_color, mark_all, pofi):
    
    plt.scatter(x=data[x], y=data[y], s=1, label="Not significant", color=ns_color)

    down = data[(data[x] >= fc_threshold_upper) & (data[y] >= sig_threshold)]
    up = data[(data[x] <= fc_threshold_lower) & (data[y] >= sig_threshold)]
    plt.scatter(x=down[x], y=down[y], s=3, label="Up-regulated", color=ur_color)
    plt.scatter(x=up[x], y=up[y], s=3, label="Down-regulated", color=dr_color)

    texts = []
    for i in range(len(data)):
        if mark_all:
            if data[x][i] >= fc_threshold_upper and data[y][i] >= sig_threshold:
                texts.append(plt.text(data[x][i], data[y][i], data[name][i], fontsize=8, color='black'))
            elif data[x][i] <= fc_threshold_lower and data[y][i] >= sig_threshold:
                texts.append(plt.text(data[x][i], data[y][i], data[name][i], fontsize=8, color='black'))
        if data[name][i] in pofi:
            texts.append(plt.text(data[x][i], data[y][i], data[name][i], fontsize=8))
    adjust_text(texts)

    plt.xlabel(x)
    plt.ylabel(y)
    plt.axvline(fc_threshold_lower, color="grey", linestyle="--")
    plt.axvline(fc_threshold_upper, color="grey", linestyle="--")
    plt.axhline(sig_threshold, color="grey", linestyle="--")
    if show_labels:
        plt.legend()
    plt.show()

def main():
    data = pd.read_csv('test.csv')
    user_input = get_user_input()
    x, y, name, fc_threshold_lower, fc_threshold_upper, sig_threshold, show_labels, ns_color, ur_color, dr_color, mark_all, pofi = user_input
    valid_pofi = check_pofi_in_data(pofi, data, name)
    plot_volcano(data, x, y, name, fc_threshold_lower, fc_threshold_upper, sig_threshold, show_labels, ns_color, ur_color, dr_color, mark_all, valid_pofi)

if __name__ == "__main__":
    main()