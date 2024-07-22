import tkinter as tk
from tkinter import filedialog, messagebox
import pyzipper

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("File Compression & Encryption")
        
        # Create widgets
        self.label = tk.Label(root, text="Drag and drop file here:")
        self.label.pack(pady=10)
        
        self.drop_area = tk.Listbox(root, width=50, height=5)
        self.drop_area.pack(pady=10)
        self.drop_area.bind('<Button-1>', self.add_file)
        
        self.password_label = tk.Label(root, text="Enter Password:")
        self.password_label.pack()
        
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()
        
        self.compress_button = tk.Button(root, text="Compress & Encrypt", command=self.compress_encrypt)
        self.compress_button.pack(pady=10)
        
        self.output_label = tk.Label(root, text="Output ZIP file:")
        self.output_label.pack()
        
        self.output_text = tk.Text(root, height=2, width=50)
        self.output_text.pack()
        
    def add_file(self, event):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.drop_area.insert(tk.END, file_path)
    
    def compress_encrypt(self):
        files_to_compress = list(self.drop_area.get(0, tk.END))
        password = self.password_entry.get()
        
        if not files_to_compress:
            messagebox.showerror("Error", "No file selected.")
            return
        
        if not password:
            messagebox.showerror("Error", "Please enter a password.")
            return
        
        try:
            with pyzipper.AESZipFile('encrypted.zip', 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zf:
                for file_path in files_to_compress:
                    zf.write(file_path, arcname=file_path.split('/')[-1])
                
                zf.setpassword(password.encode())
                
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "encrypted.zip")
            messagebox.showinfo("Success", "Compression and encryption complete.")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
