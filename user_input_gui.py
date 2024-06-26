import tkinter as tk
from tkinter import filedialog, colorchooser
import pandas as pd

def get_user_input():
    def browse_file():
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        data.set(filename)
        load_columns()

    def load_columns():
        df = pd.read_csv(data.get())
        columns = list(df.columns)
        x.set(columns[0])
        y.set(columns[1])
        name.set(columns[2])
        x_menu['menu'].delete(0, 'end')
        y_menu['menu'].delete(0, 'end')
        name_menu['menu'].delete(0, 'end')
        for col in columns:
            x_menu['menu'].add_command(label=col, command=tk._setit(x, col))
            y_menu['menu'].add_command(label=col, command=tk._setit(y, col))
            name_menu['menu'].add_command(label=col, command=tk._setit(name, col))

    def choose_ns_color():
        color_code = colorchooser.askcolor(title="Choose a color")[1]
        ns_color.set(color_code)

    def choose_ur_color():
        color_code = colorchooser.askcolor(title="Choose a color")[1]
        ur_color.set(color_code)

    def choose_dr_color():
        color_code = colorchooser.askcolor(title="Choose a color")[1]
        dr_color.set(color_code)

    def submit():
        result = {
            'title': title.get(),
            'data': pd.read_csv(data.get()),
            'x': x.get(),
            'y': y.get(),
            'name': name.get(),
            'fc_threshold_lower': float(fc_threshold_lower.get()),
            'fc_threshold_upper': float(fc_threshold_upper.get()),
            'sig_threshold': float(sig_threshold.get()),
            'show_labels': show_labels.get(),
            'ns_color': ns_color.get(),
            'ur_color': ur_color.get(),
            'dr_color': dr_color.get(),
            'mark_all': mark_all.get(),
            'pofi': points_of_interest.get().split(', ')
        }
        root.quit()
        root.destroy()
        global user_inputs
        user_inputs = result

    root = tk.Tk()
    root.title("User Input")

    title = tk.StringVar()
    data = tk.StringVar()
    x = tk.StringVar()
    y = tk.StringVar()
    name = tk.StringVar()
    fc_threshold_lower = tk.StringVar()
    fc_threshold_upper = tk.StringVar()
    sig_threshold = tk.StringVar()
    ns_color = tk.StringVar()
    ur_color = tk.StringVar()
    dr_color = tk.StringVar()
    show_labels = tk.BooleanVar()
    mark_all = tk.BooleanVar()
    points_of_interest = tk.StringVar()

    tk.Label(root, text="Plot Title").grid(row=0, column=0)
    tk.Entry(root, textvariable=title).grid(row=0, column=1, columnspan=2)

    tk.Label(root, text="Data File").grid(row=1, column=0)
    tk.Entry(root, textvariable=data).grid(row=1, column=1)
    tk.Button(root, text="Browse", command=browse_file).grid(row=1, column=2)

    tk.Label(root, text="X-axis Column").grid(row=2, column=0)
    x_menu = tk.OptionMenu(root, x, "")
    x_menu.grid(row=2, column=1)

    tk.Label(root, text="Y-axis Column").grid(row=3, column=0)
    y_menu = tk.OptionMenu(root, y, "")
    y_menu.grid(row=3, column=1)

    tk.Label(root, text="Name Column").grid(row=4, column=0)
    name_menu = tk.OptionMenu(root, name, "")
    name_menu.grid(row=4, column=1)

    tk.Label(root, text="FC Threshold Lower").grid(row=5, column=0)
    tk.Entry(root, textvariable=fc_threshold_lower).grid(row=5, column=1)

    tk.Label(root, text="FC Threshold Upper").grid(row=6, column=0)
    tk.Entry(root, textvariable=fc_threshold_upper).grid(row=6, column=1)

    tk.Label(root, text="Significance Threshold").grid(row=7, column=0)
    tk.Entry(root, textvariable=sig_threshold).grid(row=7, column=1)

    tk.Checkbutton(root, text="Show Labels", variable=show_labels).grid(row=8, column=0, columnspan=2)
    
    tk.Label(root, text="Non-Significant Color").grid(row=9, column=0)
    tk.Entry(root, textvariable=ns_color).grid(row=9, column=1)
    tk.Button(root, text="Choose Color", command=choose_ns_color).grid(row=9, column=2)

    tk.Label(root, text="Upregulated Color").grid(row=10, column=0)
    tk.Entry(root, textvariable=ur_color).grid(row=10, column=1)
    tk.Button(root, text="Choose Color", command=choose_ur_color).grid(row=10, column=2)

    tk.Label(root, text="Downregulated Color").grid(row=11, column=0)
    tk.Entry(root, textvariable=dr_color).grid(row=11, column=1)
    tk.Button(root, text="Choose Color", command=choose_dr_color).grid(row=11, column=2)

    tk.Checkbutton(root, text="Mark All", variable=mark_all).grid(row=12, column=0, columnspan=2)

    tk.Label(root, text="Points of Interest").grid(row=13, column=0)
    tk.Entry(root, textvariable=points_of_interest).grid(row=13, column=1)

    tk.Button(root, text="Submit", command=submit).grid(row=14, column=0, columnspan=3)

    root.mainloop()

    return user_inputs

