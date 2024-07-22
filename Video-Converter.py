import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import *

def browse_file():
    filepath = filedialog.askopenfilename()
    entry_file_path.delete(0, tk.END)
    entry_file_path.insert(0, filepath)

def select_output_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".mp4",
                                            filetypes=[("MP4 files", "*.mp4"),
                                                       ("AVI files", "*.avi"),
                                                       ("All files", "*.*")])
    entry_output_path.delete(0, tk.END)
    entry_output_path.insert(0, filepath)

def convert_video():
    input_path = entry_file_path.get()
    output_path = entry_output_path.get()

    if input_path == "":
        messagebox.showerror("Error", "Please select an input file.")
        return
    
    if output_path == "":
        messagebox.showerror("Error", "Please specify an output file path.")
        return

    try:
        video = VideoFileClip(input_path)
        video.write_videofile(output_path)
        messagebox.showinfo("Success", f"Conversion successful!\nInput File: {input_path}\nOutput File: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Error during conversion: {str(e)}")

root = tk.Tk()
root.title("Video Converter")

label_file_path = tk.Label(root, text="Select Input File:")
label_file_path.grid(row=0, column=0, padx=10, pady=10)
entry_file_path = tk.Entry(root, width=50)
entry_file_path.grid(row=0, column=1, padx=10, pady=10)

button_browse = tk.Button(root, text="Browse", command=browse_file)
button_browse.grid(row=0, column=2, padx=10, pady=10)

label_output_path = tk.Label(root, text="Save as:")
label_output_path.grid(row=1, column=0, padx=10, pady=10)
entry_output_path = tk.Entry(root, width=50)
entry_output_path.grid(row=1, column=1, padx=10, pady=10)

button_select_output = tk.Button(root, text="Select Output", command=select_output_file)
button_select_output.grid(row=1, column=2, padx=10, pady=10)

button_convert = tk.Button(root, text="Convert", command=convert_video)
button_convert.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
