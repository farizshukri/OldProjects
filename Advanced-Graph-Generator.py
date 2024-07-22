import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk

# Function to plot the graph based on user input
def plot_graph():
    equation = entry_equation.get()
    function_type = combo_function_type.get()

    try:
        if function_type == 'Linear':
            x = np.linspace(-10, 10, 400)
            y = eval(equation)
            plot_title = f'Graph of {equation} (Linear)'

        elif function_type == 'Trigonometric':
            x = np.linspace(-2*np.pi, 2*np.pi, 400)
            y = eval(equation)
            plot_title = f'Graph of {equation} (Trigonometric)'

        elif function_type == 'Custom':
            x_range = eval(entry_x_range.get())
            x = np.linspace(x_range[0], x_range[1], 400)
            y = eval(equation)
            plot_title = f'Custom Graph of {equation}'

        else:
            raise ValueError("Invalid function type selected.")

        # Clear previous plot, if any
        ax.clear()

        # Plotting the graph
        ax.plot(x, y)
        ax.set_title(plot_title)
        ax.grid(True)
        canvas.draw()

    except Exception as e:
        lbl_status.config(text=f"Error: {e}")

# Create main window
root = tk.Tk()
root.title("Advanced Mathematical Graph Generator")

# Create input frame
frame_input = ttk.Frame(root, padding="10")
frame_input.pack()

lbl_equation = ttk.Label(frame_input, text="Enter equation:")
lbl_equation.grid(row=0, column=0, padx=10, pady=5)

entry_equation = ttk.Entry(frame_input, width=30)
entry_equation.grid(row=0, column=1, padx=10, pady=5)

lbl_function_type = ttk.Label(frame_input, text="Select function type:")
lbl_function_type.grid(row=1, column=0, padx=10, pady=5)

function_types = ['Linear', 'Trigonometric', 'Custom']
combo_function_type = ttk.Combobox(frame_input, values=function_types, state="readonly", width=20)
combo_function_type.current(0)  # Set default selection
combo_function_type.grid(row=1, column=1, padx=10, pady=5)

lbl_x_range = ttk.Label(frame_input, text="Custom x-range (start, end):")
lbl_x_range.grid(row=2, column=0, padx=10, pady=5)

entry_x_range = ttk.Entry(frame_input, width=20)
entry_x_range.grid(row=2, column=1, padx=10, pady=5)
entry_x_range.insert(tk.END, "[-10, 10]")  # Default value

btn_plot = ttk.Button(frame_input, text="Plot Graph", command=plot_graph)
btn_plot.grid(row=3, columnspan=2, padx=10, pady=10)

# Create status label
lbl_status = ttk.Label(root, text="", padding="10")
lbl_status.pack()

# Create matplotlib figure and axes
fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('y')

# Create tkinter canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Start the GUI main loop
root.mainloop()
