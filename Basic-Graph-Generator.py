import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

def plot_graph():
    equation = entry_equation.get()
    try:
        x = range(-10, 11)
        y = [eval(equation) for x in x]
        
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title(f'Graph of {equation}')
        ax.grid(True)
        
        # Embedding matplotlib graph into tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame_graph)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
    except Exception as e:
        lbl_status.config(text=f"Error: {e}")

# Create main window
root = tk.Tk()
root.title("Mathematical Graph Generator")

# Create input frame
frame_input = ttk.Frame(root, padding="10")
frame_input.pack()

lbl_equation = ttk.Label(frame_input, text="Enter equation (e.g., x**2 + 2*x - 3):")
lbl_equation.grid(row=0, column=0, padx=10, pady=5)

entry_equation = ttk.Entry(frame_input, width=30)
entry_equation.grid(row=0, column=1, padx=10, pady=5)

btn_plot = ttk.Button(frame_input, text="Plot Graph", command=plot_graph)
btn_plot.grid(row=0, column=2, padx=10, pady=5)

# Create status label
lbl_status = ttk.Label(root, text="", padding="10")
lbl_status.pack()

# Create graph frame
frame_graph = ttk.Frame(root)
frame_graph.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
