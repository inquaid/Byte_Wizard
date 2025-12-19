import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import threading


def on_enter(e):
    """Change button appearance when mouse enters"""
    e.widget.config(bg='#A6B1E1', fg='#FFFFFF')


def on_leave(event):
    """Restore button appearance when mouse leaves"""
    event.widget.config(bg='#DCD6F7', fg='#424874')


def show_loading_screen(root):
    """Display a loading screen with progress bar"""
    loading_window = tk.Toplevel(root)
    loading_window.title("Installing")
    loading_window.geometry("300x150")
    
    # Center the loading window
    loading_window.update_idletasks()
    x = (loading_window.winfo_screenwidth() // 2) - (loading_window.winfo_width() // 2)
    y = (loading_window.winfo_screenheight() // 2) - (loading_window.winfo_height() // 2)
    loading_window.geometry(f"+{x}+{y}")
    
    # Add a professional looking loading interface
    label = tk.Label(loading_window, text="Installation in progress...", font=('Inter', 12))
    label.pack(pady=20)
    
    progress = ttk.Progressbar(loading_window, mode='indeterminate')
    progress.pack(pady=10, padx=20, fill='x')
    progress.start()
    
    return loading_window


def run_batch_file(batch_file_path, root, loading_window):
    """Execute batch file and handle its output"""
    try:
        res = subprocess.run([batch_file_path], capture_output=True, text=True, check=True)
        output = "Installation completed successfully ✅"
    except subprocess.CalledProcessError as e:
        output = f"Error during installation: {e.output}"
    except FileNotFoundError:
        output = f"The installation script '{batch_file_path}' was not found."
    finally:
        loading_window.destroy()
        messagebox.showinfo("Installation Status", output)


def install_software(root, script_path):
    """Start the installation process in a separate thread"""
    loading_window = show_loading_screen(root)
    task_thread = threading.Thread(target=run_batch_file, args=(script_path, root, loading_window))
    task_thread.start()


# Installation function definitions
def install_chocolatey(root):
    install_software(root, "src/scripts/installers/chocolatey.bat")


def install_mingw(root):
    install_software(root, "src/scripts/installers/mingw.bat")


def install_python(root):
    install_software(root, "src/scripts/installers/python.bat")


def install_java(root):
    install_software(root, "src/scripts/installers/java.bat")


def install_vscode(root):
    install_software(root, "src/scripts/installers/vscode.bat")


def install_netbeans(root):
    install_software(root, "src/scripts/installers/netbeans.bat")


def install_jetbrains(root):
    install_software(root, "src/scripts/installers/jetbrains.bat")


def install_codeblocks(root):
    install_software(root, "src/scripts/installers/codeblocks.bat")


def install_iverilog(root):
    install_software(root, "src/scripts/installers/iverilog.bat")


def install_gtkwave(root):
    install_software(root, "src/scripts/installers/gtkwave.bat") 