from second_window import *


def on_enter(e):
    e.widget.config(bg='#A6B1E1', fg='#FFFFFF')


def on_leave(event):
    event.widget.config(bg='#DCD6F7', fg='#424874')


def Install_Choco(root):
    go_go(root, "choco_install.bat")


# btn = tk.Button(root, text="Click", command=lambda: go_go(root, file_path))

# print("choco")
# print("choco")


def Install_C(root):
    go_go(root, "mingw_install.bat")
    # print("C C++")


def Install_Python(root):
    go_go(root, "python_install.bat")
    # print("Python")


def Install_Java(root):
    go_go(root, "java_install.bat")
    # print("JAVA")


def Install_vsc(root):
    go_go(root, "vsc_install.bat")
    # print("VS CODE")


def Install_NetBeans(root):
    go_go(root, "netbeans_install.bat")
    # print("NetBeans")


def Install_Jetbrain(root):
    go_go(root, "jetbrain_install.bat")
    # print("jetbrain")


def Install_CodeBlocks(root):
    go_go(root, "code_blocks_install.bat")
    # print("code blocks")
