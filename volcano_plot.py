import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from adjustText import adjust_text
import user_input_gui

# reference: https://resources.qiagenbioinformatics.com/manuals/rnaanalysisportal/current/index.php?manual=Volcano_plot.html

# def get_user_input():
#     # User input - for testing only, replace with actual user input as needed
#     data = pd.read_csv('test.csv') # select from drive
#     x = 'Log2FC' # select from columns
#     y = 'minuslog10(pval)' # select from columns
#     name = 'Name' # sekect from columns
#     fc_threshold_lower = -1 # user input
#     fc_threshold_upper = 1 # user input
#     sig_threshold = 0.5 # user input
#     show_labels = False # check box
#     ns_color = 'lightgrey' # select from color picker
#     ur_color = 'deepskyblue' # select from color picker
#     dr_color = 'orangered' # select from color picker
#     mark_all = True # check box
    
#     # Points of interest input
#     pofi = input('Enter the name of points of interest (comma separated):').split(', ')  # user input
    
#     return (data, x, y, name, fc_threshold_lower, fc_threshold_upper, sig_threshold, show_labels, ns_color, ur_color, dr_color, mark_all, pofi)

def check_pofi_in_data(pofi, data, name):
    valid_pofi = []
    if not pofi:
        print("No points of interest selected")
    else:
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
    adjust_text(texts, arrowprops=dict(arrowstyle="-", color='black', lw=0.5))

    plt.xlabel(x)
    plt.ylabel(y)
    plt.axvline(fc_threshold_lower, color="grey", linestyle="--")
    plt.axvline(fc_threshold_upper, color="grey", linestyle="--")
    plt.axhline(sig_threshold, color="grey", linestyle="--")
    if show_labels:
        plt.legend()
    plt.show()

def main():
    user_inputs = user_input_gui.get_user_input()
    data = user_inputs['data']
    x = user_inputs['x']
    y = user_inputs['y']
    name = user_inputs['name']
    fc_threshold_lower = user_inputs['fc_threshold_lower']
    fc_threshold_upper = user_inputs['fc_threshold_upper']
    sig_threshold = user_inputs['sig_threshold']
    show_labels = user_inputs['show_labels']
    ns_color = user_inputs['ns_color']
    ur_color = user_inputs['ur_color']
    dr_color = user_inputs['dr_color']
    mark_all = user_inputs['mark_all']
    pofi = user_inputs['pofi']
    valid_pofi = check_pofi_in_data(pofi, data, name)
    plot_volcano(data, x, y, name, fc_threshold_lower, fc_threshold_upper, sig_threshold, show_labels, ns_color, ur_color, dr_color, mark_all, valid_pofi)

if __name__ == "__main__":
    main()

