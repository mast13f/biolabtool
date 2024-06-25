
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from adjustText import adjust_text


# volcano plot
# more here: https://resources.qiagenbioinformatics.com/manuals/rnaanalysisportal/current/index.php?manual=Volcano_plot.html

# user input
# x = input('x:')
# y = input('y:')
# name = input('name:')
# fc_threshold_lower = float(input('fc_threshold_lower:'))
# fc_threshold_upper = float(input('fc_threshold_upper:'))
# sig_threshold = float(input('sig_threshold:'))

# user input - for testing only
x = 'Log2FC'
y = 'minuslog10(pval)'
name = 'Name'
fc_threshold_lower = -0.5
fc_threshold_upper = 0.5
sig_threshold = 0.5
data = pd.read_csv('test.csv')

### settings

# show labels?
# show_labels = input('Show labels? (y/n):')
# if show_labels == 'y':
#     show_labels = True
# else:
#     show_labels = False

# colors?
# ns_color = input('Not significant color:') #'lightgrey'
# ur_color = input('Up-regulated color:') # 'deepskyblue'
# dr_color = input('Down-regulated color:') # 'orangered'

# mark all
# mark_all = input('Mark all? (y/n):')
# if mark_all == 'y':
#     mark_all = True
# else:
#     mark_all = False

# points of interest
pofi = input('Points of interest? (y/n):')
if pofi == 'y':
    pofi = input('Enter the name of points of interest (comma separated):').split(',')
    # test if the points of interest are in the data
    for poi in pofi:
        if poi not in data[name].values:
            print(f'{poi} not found in the data')
            pofi.remove(poi)
else:
    pofi = []




def volcano_plot(data, x, y, name, fc_threshold_lower, fc_threshold_upper, sig_threshold, 
                 show_labels=False, ns_color='lightgrey', ur_color='deepskyblue', dr_color='orangered', mark_all=False,
                 pofi=[]):
    
    # not significant
    plt.scatter(x=data[x], y=data[y], s=1, label="Not significant", color=ns_color)

    # highlight down- or up- regulated genes
    down = data[(data[x] >= fc_threshold_upper) & (data[y] >= sig_threshold)]
    up = data[(data[x] <= fc_threshold_lower) & (data[y] >= sig_threshold)]
    plt.scatter(x=down[x], y=down[y], s=3, label="Up-regulated", color=ur_color)
    plt.scatter(x=up[x], y=up[y], s=3, label="Down-regulated", color=dr_color)

    # adjust text to avoid overlapping
    texts = []
    for i in range(len(data)):
        if mark_all:
            if data[x][i] >= fc_threshold_upper and data[y][i] >= sig_threshold:
                texts.append(plt.text(data[x][i], data[y][i], data[name][i], fontsize=8, color='black'))
            elif data[x][i] <= fc_threshold_lower and data[y][i] >= sig_threshold:
                texts.append(plt.text(data[x][i], data[y][i], data[name][i], fontsize=8, color='black'))
        if data[name][i] in pofi:
            texts.append(plt.text(data[x][i], data[y][i], data[name][i], fontsize=8))  # Change color to red
    adjust_text(texts)

    plt.xlabel(x)
    plt.ylabel(y)
    plt.axvline(fc_threshold_lower, color="grey", linestyle="--")
    plt.axvline(fc_threshold_upper, color="grey", linestyle="--")
    plt.axhline(sig_threshold, color="grey", linestyle="--")
    if show_labels:
        plt.legend()
    plt.show()


volcano_plot(data, x, y, name, fc_threshold_lower, fc_threshold_upper, sig_threshold, pofi=pofi)

