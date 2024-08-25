import tkinter as tk
from tkinter import PhotoImage
from my_functions import *

# main window
root = tk.Tk()
root.geometry('500x500')
root.minsize(400, 700)
# root.resizable(False, False)
root.config(background='#F4EEFF')
root.title('ByteWizard')
# icon = PhotoImage(file='wizard1.png')
# root.iconphoto(True, icon)

label = tk.Label(
    root,
    text="Wizzard's Tools",
    fg='#424874',
    bg='#F4EEFF',
    height=2,
    width=30,
    font=('inter', 30),
)
label.pack()

# MUST label
label2 = tk.Label(
    root,
    text="  Must",
    fg='#424874',
    bg='#A6B1E1',
    height=1,
    width=30,
    font=('inter', 15, "bold"),
    anchor="w",
)
label2.pack(pady=5, fill="x")

# chocolatey button
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
    tk.Button(root, text="🍫 Chocolatey", **btn_style, command=lambda: Install_Choco(root)),
    #     btn = tk.Button(root, text="Click", command=lambda: go_go(root, file_path))

]

for btn in buttons:
    btn.pack(pady=10)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# language label
label_lang = tk.Label(
    root,
    text="  Language",
    fg='#424874',
    bg='#A6B1E1',
    height=1,
    width=30,
    font=('inter', 15, "bold"),
    anchor="w",
)
label_lang.pack(pady=5, fill="x")

# c/cpp , python , java
buttons = [
    tk.Button(root, text="C/C++", **btn_style, command=lambda: Install_C(root)),
    tk.Button(root, text="Python", **btn_style, command=lambda: Install_Python(root)),
    tk.Button(root, text="Java", **btn_style, command=lambda: Install_Java(root)),
]

for btn in buttons:
    btn.pack(pady=10)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# IDE label
Label_IDE = tk.Label(
    root,
    text="  IDE",
    fg='#424874',
    bg='#A6B1E1',
    height=1,
    width=30,
    font=('inter', 15, "bold"),
    anchor="w",
)
Label_IDE.pack(pady=5, fill="x")

# VSC, netbeans, intelijee, code blocks
buttons = [
    tk.Button(root, text="VS CODE", **btn_style, command=lambda: Install_vsc(root)),
    tk.Button(root, text="NetBeans", **btn_style, command=lambda: Install_NetBeans(root)),
    tk.Button(root, text="Jetbrain", **btn_style, command=lambda: Install_Jetbrain(root)),
    tk.Button(root, text="Code Blocks", **btn_style, command=lambda: Install_CodeBlocks(root)),
]

for btn in buttons:
    btn.pack(pady=10)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

root.mainloop()

