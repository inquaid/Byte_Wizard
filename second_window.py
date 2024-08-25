import tkinter as tk
from tkinter import ttk
import subprocess
import threading


def show_output_messagebox(root, output):
    messagebox.showinfo("Output", output)


def show_loading_screen(root):
    loading_window = tk.Toplevel(root)
    loading_window.title("Loading")
    loading_window.geometry("200x100")

    loading_window.update_idletasks()
    x = (loading_window.winfo_screenwidth() // 2) - (loading_window.winfo_width() // 2)
    y = (loading_window.winfo_screenheight() // 2) - (loading_window.winfo_height() // 2)
    loading_window.geometry(f"+{x}+{y}")

    label = tk.Label(loading_window, text="Processing...", font=('Helvetica', 12))
    label.pack(pady=20)

    progress = ttk.Progressbar(loading_window, mode='indeterminate')
    progress.pack(pady=10, padx=20, fill='x')
    progress.start()

    return loading_window


def run_batch_file(batch_file_path, root, loading_window):
    try:
        res = subprocess.run([batch_file_path], capture_output=True, text=True, check=True)
        output = "green checkmark✅"
    except subprocess.CalledProcessError as e:
        output = f"Error: {e.output}"
    except FileNotFoundError:
        output = f"The batch file '{batch_file_path}' was not found."
    finally:
        loading_window.destroy()
        show_output_messagebox(root, output)


def go_go(root, file_path):
    loading_window = show_loading_screen(root)
    task_thread = threading.Thread(target=run_batch_file, args=(file_path, root, loading_window))
    task_thread.start()


import tkinter as tk
from tkinter import messagebox

file_path = "ptc.bat"


# def open(root):
#     btn = tk.Button(root, text="Click", command=lambda: go_go(root, file_path))
#     btn.pack()


# root = tk.Tk()
# root.geometry("200x100")
# open(root)
# root.mainloop()
