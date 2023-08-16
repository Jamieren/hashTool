import hashlib
import tkinter as tk
from tkinter import simpledialog, scrolledtext
from tkinter import ttk
from tkinter import messagebox

# Author: Jamie Ren
# Date: August 16th, 2023

# The Hashing Tool application is a user-friendly graphical interface that
# allows users to quickly and easily generate hash values for text input 
# using a variety of popular hash algorithms. 

# It offers a straightforward and intuitive way to perform hash calculations, 
# making it suitable for users who need to generate hash values for 
# security, data integrity, or verification purposes.



class HashToolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hashing Tool")

        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Helvetica", 12))
        self.style.configure("TButton", font=("Helvetica", 12))

        self.instructions_text = (
            "\nWelcome to the Hashing Tool!\n\n"
            "Enter the text you want to hash in the text entry below.\n\n"
            "Click the 'Hash' button.\n\n"
            "Then select the hash algorithms you'd like to use.\n\n"
            "Finally, click 'OK' to calculate and display the hashed results.\n\n"
            "Thanks for using!"
        )

        self.instructions_box = tk.Text(root, wrap=tk.WORD, height=15, width=50)
        self.instructions_box.insert("insert", self.instructions_text)
        self.instructions_box.configure(state="disabled")
        self.instructions_box.pack(pady=10)

        self.text_entry = ttk.Entry(root, font=("Helvetica", 12), width=40)
        self.text_entry.pack(pady=5)

        self.hash_button = ttk.Button(root, text="Hash", command=self.hash_text)
        self.hash_button.pack(pady=5)
    def hash_text(self):
        text = self.text_entry.get().strip()
        if not text:
            messagebox.showerror("Error", "Please enter text to hash.")
            return

        selected_algorithms = self.select_algorithms()

        if not selected_algorithms:
            return

        results = self.calculate_hashes(text, selected_algorithms)
        self.show_results("Hashed Results", results)

    def select_algorithms(self):
        options = [
            "md5", "sha1", "sha256", "sha224", "sha384",
            "sha512", "blake2s", "blake2b", "sha3_256", "whirlpool"
        ]
        selected = []

        dialog = tk.Toplevel(self.root)
        dialog.title("Algorithm Selection")
        dialog.geometry("200x300")  # Adjust the size of the selection window

        for algo in options:
            var = tk.IntVar()
            checkbox = tk.Checkbutton(dialog, text=algo.upper(), variable=var)
            checkbox.pack(anchor="w")
            selected.append((algo, var))

        tk.Button(dialog, text="OK", command=dialog.destroy).pack()

        dialog.grab_set()
        dialog.wait_window()

        return [algo for algo, var in selected if var.get() == 1]

    def calculate_hashes(self, text, algorithms):
        results = []
        for algorithm in algorithms:
            hashed = self.hash(text, algorithm)
            results.append(f"{algorithm.upper()}: {hashed}")
        return results

    def show_results(self, title, results):
        result_window = tk.Toplevel(self.root)
        result_window.title(title)
        text_box = scrolledtext.ScrolledText(result_window, wrap=tk.WORD)
        text_box.insert("insert", "\n".join(results))
        text_box.pack(fill="both", expand=True)
        text_box.configure(state="disabled")
        
        result_window.update_idletasks()  # Force update the layout

    def hash(self, text, algorithm):
        hash_object = hashlib.new(algorithm)
        hash_object.update(text.encode('utf-8'))
        return hash_object.hexdigest()

def main():
    root = tk.Tk()
    root.geometry("500x400")  # Set the initial size of the window
    app = HashToolApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
