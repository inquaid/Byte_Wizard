import tkinter as tk
from tkinter import PhotoImage
from my_functions import *

# Main window
root = tk.Tk()
root.geometry('500x500')
root.minsize(400, 600)
root.config(background='#F4EEFF')
root.title('ByteWizard')
# icon = PhotoImage(file='wizard1.png')
# root.iconphoto(True, icon)

# Create a frame to hold the canvas and scrollbars
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create a canvas widget
canvas = tk.Canvas(frame, bg='#F4EEFF')
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a vertical scrollbar
v_scroll = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
v_scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Add a horizontal scrollbar (optional, if needed)
# h_scroll = tk.Scrollbar(frame, orient=tk.HORIZONTAL, command=canvas.xview)
# h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

# Configure the canvas scrollbars
canvas.configure(yscrollcommand=v_scroll.set)
# canvas.configure(xscrollcommand=h_scroll.set)  # Uncomment if using horizontal scrollbar

# Create a frame inside the canvas to hold other widgets
inner_frame = tk.Frame(canvas, bg='#F4EEFF')
inner_frame_id = canvas.create_window((0, 0), window=inner_frame, anchor="nw")

def configure_canvas(event):
    # Update the scroll region of the canvas to the size of the inner frame
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_resize(event):
    # Update the canvas size to match the window size
    canvas_width = event.width
    canvas.itemconfig(inner_frame_id, width=canvas_width)

def on_mouse_wheel(event):
    # Adjust scrolling sensitivity
    sensitivity = 1  # Adjust this value for smoother or faster scrolling
    if event.delta:  # For Windows and Linux
        canvas.yview_scroll(int(-1 * (event.delta / 120) * sensitivity), "units")
    else:  # For macOS
        canvas.yview_scroll(int(-1 * (event.num - 4) * sensitivity), "units")


def on_click(event):
    # Save the current mouse position
    canvas.scan_mark(event.x, event.y)

def on_drag(event):
    # Scroll the canvas content based on the mouse drag
    canvas.scan_dragto(event.x, event.y, gain=1)

# Bind the canvas to the scrollbars and resizing events
inner_frame.bind("<Configure>", configure_canvas)
canvas.bind("<Configure>", on_resize)

# Bind touch drag events
canvas.bind("<Button-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)

# Mouse wheel event bindings
canvas.bind_all("<MouseWheel>", on_mouse_wheel)  # Windows and Linux
canvas.bind_all("<Button-4>", on_mouse_wheel)    # macOS up scroll
canvas.bind_all("<Button-5>", on_mouse_wheel)    # macOS down scroll

# Adding widgets to the inner frame (your existing code)

label = tk.Label(
    inner_frame,
    text="Wizzard's Tools",
    fg='#424874',
    bg='#F4EEFF',
    height=2,
    width=30,
    font=('inter', 30),
)
label.pack()

label2 = tk.Label(
    inner_frame,
    text="  Must",
    fg='#424874',
    bg='#A6B1E1',
    height=1,
    width=30,
    font=('inter', 15, "bold"),
    anchor="w",
)
label2.pack(pady=5, fill="x")

btn_style = {
    'font': ("Inter", 15),
    'borderwidth': 1,
    'highlightthickness': 0,
    'relief': "flat",
    'bg': '#DCD6F7',
    'fg': '#424874',
    'height': 1,
    'width': 15
}

buttons = [
    tk.Button(inner_frame, text="🍫 Chocolatey", **btn_style, command=lambda: Install_Choco(root)),
]

for btn in buttons:
    btn.pack(pady=10)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

label_lang = tk.Label(
    inner_frame,
    text="  Language",
    fg='#424874',
    bg='#A6B1E1',
    height=1,
    width=30,
    font=('inter', 15, "bold"),
    anchor="w",
)
label_lang.pack(pady=5, fill="x")

buttons = [
    tk.Button(inner_frame, text="C/C++", **btn_style, command=lambda: Install_C(root)),
    tk.Button(inner_frame, text="Python", **btn_style, command=lambda: Install_Python(root)),
    tk.Button(inner_frame, text="Java", **btn_style, command=lambda: Install_Java(root)),
]

for btn in buttons:
    btn.pack(pady=10)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

Label_IDE = tk.Label(
    inner_frame,
    text="  IDE",
    fg='#424874',
    bg='#A6B1E1',
    height=1,
    width=30,
    font=('inter', 15, "bold"),
    anchor="w",
)
Label_IDE.pack(pady=5, fill="x")

buttons = [
    tk.Button(inner_frame, text="VS CODE", **btn_style, command=lambda: Install_vsc(root)),
    tk.Button(inner_frame, text="NetBeans", **btn_style, command=lambda: Install_NetBeans(root)),
    tk.Button(inner_frame, text="Jetbrain", **btn_style, command=lambda: Install_Jetbrain(root)),
    tk.Button(inner_frame, text="Code Blocks", **btn_style, command=lambda: Install_CodeBlocks(root)),
]

for btn in buttons:
    btn.pack(pady=10)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

Simulator = tk.Label(
    inner_frame,
    text="  SIMULATOR",
    fg='#424874',
    bg='#A6B1E1',
    height=1,
    width=30,
    font=('inter', 15, "bold"),
    anchor="w",
)
Simulator.pack(pady=5, fill="x")

buttons = [
    tk.Button(inner_frame, text="Iverilog", **btn_style, command=lambda: Install_Iverilog(root)),
    tk.Button(inner_frame, text="GtkWave", **btn_style, command=lambda: Install_Gtkwave(root)),
]

for btn in buttons:
    btn.pack(pady=10)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

root.mainloop()
