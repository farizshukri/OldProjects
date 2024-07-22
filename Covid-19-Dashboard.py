import random

def fetch_data():
    # Simulated COVID-19 data (replace with actual API call in real scenario)
    data = {
        'cases': random.randint(100000, 500000),
        'deaths': random.randint(5000, 30000),
        'recovered': random.randint(50000, 200000),
        'active': random.randint(50000, 250000)
    }
    return data

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to update data and refresh dashboard
def refresh_data():
    data = fetch_data()
    label_confirmed.config(text=f"Confirmed Cases: {data['cases']}")
    label_deaths.config(text=f"Deaths: {data['deaths']}")
    label_recovered.config(text=f"Recovered: {data['recovered']}")
    label_active.config(text=f"Active Cases: {data['active']}")

# Function to plot pie chart
def plot_chart():
    data = fetch_data()
    labels = ['Active', 'Recovered', 'Deaths']
    sizes = [data['active'], data['recovered'], data['deaths']]
    
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    
    # Display pie chart in tkinter window
    chart = FigureCanvasTkAgg(fig, root)
    chart.get_tk_widget().grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create main tkinter window
root = tk.Tk()
root.title("COVID-19 Dashboard")

# Labels to display statistics
label_confirmed = ttk.Label(root, text="Confirmed Cases: ")
label_confirmed.grid(row=0, column=0, padx=10, pady=10, sticky='w')

label_deaths = ttk.Label(root, text="Deaths: ")
label_deaths.grid(row=1, column=0, padx=10, pady=10, sticky='w')

label_recovered = ttk.Label(root, text="Recovered: ")
label_recovered.grid(row=0, column=1, padx=10, pady=10, sticky='w')

label_active = ttk.Label(root, text="Active Cases: ")
label_active.grid(row=1, column=1, padx=10, pady=10, sticky='w')

# Button to refresh data
button_refresh = ttk.Button(root, text="Refresh Data", command=refresh_data)
button_refresh.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Button to plot pie chart
button_plot = ttk.Button(root, text="Show Pie Chart", command=plot_chart)
button_plot.grid(row=2, column=1, padx=10, pady=10)

# Fetch initial data and display
refresh_data()

# Start the tkinter main loop
root.mainloop()
