import tkinter as tk
from tkinter import filedialog, colorchooser
from tkinter import ttk
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
            name_menu['menu'].add_command(label=col, command=tk._setit(name, col, name_updated))

    def name_updated(*args):
        df = pd.read_csv(data.get())
        selected_name_col = name.get()
        update_points_of_interest_list(df[selected_name_col].values)

    def update_points_of_interest_list(items):
        pofi_listbox.delete(0, tk.END)
        for item in items:
            pofi_listbox.insert(tk.END, item)

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
        selected_pofi = [pofi_listbox.get(i) for i in pofi_listbox.curselection()]
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
            'pofi': selected_pofi
        }
        root.quit()
        root.destroy()
        global user_inputs
        user_inputs = result

    root = tk.Tk()
    root.title("User Input")

    # Styling
    style = ttk.Style()
    style.configure("TButton", padding=6)
    style.configure("TLabel", padding=6)
    style.configure("TEntry", padding=6)
    style.configure("TCheckbutton", padding=6)
    style.configure("TOptionMenu", padding=6)

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

    ttk.Label(root, text="Plot Title").grid(row=0, column=0, sticky="w")
    ttk.Entry(root, textvariable=title).grid(row=0, column=1, columnspan=2, sticky="ew")

    ttk.Label(root, text="Data File").grid(row=1, column=0, sticky="w")
    ttk.Entry(root, textvariable=data).grid(row=1, column=1, sticky="ew")
    ttk.Button(root, text="Browse", command=browse_file).grid(row=1, column=2, sticky="ew")

    ttk.Label(root, text="X-axis Column").grid(row=2, column=0, sticky="w")
    x_menu = ttk.OptionMenu(root, x, "")
    x_menu.grid(row=2, column=1, sticky="ew")

    ttk.Label(root, text="Y-axis Column").grid(row=3, column=0, sticky="w")
    y_menu = ttk.OptionMenu(root, y, "")
    y_menu.grid(row=3, column=1, sticky="ew")

    ttk.Label(root, text="Name Column").grid(row=4, column=0, sticky="w")
    name_menu = ttk.OptionMenu(root, name, "")
    name_menu.grid(row=4, column=1, sticky="ew")

    ttk.Label(root, text="FC Threshold Lower").grid(row=5, column=0, sticky="w")
    ttk.Entry(root, textvariable=fc_threshold_lower).grid(row=5, column=1, sticky="ew")

    ttk.Label(root, text="FC Threshold Upper").grid(row=6, column=0, sticky="w")
    ttk.Entry(root, textvariable=fc_threshold_upper).grid(row=6, column=1, sticky="ew")

    ttk.Label(root, text="Significance Threshold").grid(row=7, column=0, sticky="w")
    ttk.Entry(root, textvariable=sig_threshold).grid(row=7, column=1, sticky="ew")

    ttk.Checkbutton(root, text="Show Labels", variable=show_labels).grid(row=8, column=0, columnspan=2, sticky="w")
    
    ttk.Label(root, text="Non-Significant Color").grid(row=9, column=0, sticky="w")
    ttk.Entry(root, textvariable=ns_color).grid(row=9, column=1, sticky="ew")
    ttk.Button(root, text="Choose Color", command=choose_ns_color).grid(row=9, column=2, sticky="ew")

    ttk.Label(root, text="Upregulated Color").grid(row=10, column=0, sticky="w")
    ttk.Entry(root, textvariable=ur_color).grid(row=10, column=1, sticky="ew")
    ttk.Button(root, text="Choose Color", command=choose_ur_color).grid(row=10, column=2, sticky="ew")

    ttk.Label(root, text="Downregulated Color").grid(row=11, column=0, sticky="w")
    ttk.Entry(root, textvariable=dr_color).grid(row=11, column=1, sticky="ew")
    ttk.Button(root, text="Choose Color", command=choose_dr_color).grid(row=11, column=2, sticky="ew")

    ttk.Checkbutton(root, text="Mark All", variable=mark_all).grid(row=12, column=0, columnspan=2, sticky="w")

    ttk.Label(root, text="Points of Interest").grid(row=13, column=0, sticky="w")
    pofi_listbox = tk.Listbox(root, listvariable=points_of_interest, selectmode=tk.MULTIPLE)
    pofi_listbox.grid(row=13, column=1, sticky="ew", columnspan=2)

    ttk.Button(root, text="Submit", command=submit).grid(row=14, column=0, columnspan=3, sticky="ew")

    root.mainloop()

    return user_inputs