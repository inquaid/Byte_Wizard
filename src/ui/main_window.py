import tkinter as tk
from tkinter import ttk, PhotoImage
import sys
import os

# Add parent directory to path to import from core
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.functions import (
    on_enter, on_leave, 
    install_chocolatey, install_mingw, install_python, install_java,
    install_vscode, install_netbeans, install_jetbrains, install_codeblocks,
    install_iverilog, install_gtkwave
)

class ByteWizardApp:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_ui()
        
    def setup_window(self):
        """Configure the main window properties"""
        self.root.title('Byte Wizard - Software Installer')
        self.root.geometry('800x650')
        self.root.minsize(600, 650)
        self.root.config(background='#F4EEFF')
        
        # Try to set app icon
        try:
            icon_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 
                                     "assets", "wizard_icon.png")
            if os.path.exists(icon_path):
                icon = PhotoImage(file=icon_path)
                self.root.iconphoto(True, icon)
        except Exception as e:
            print(f"Could not load icon: {e}")
            
    def create_ui(self):
        """Create the application UI"""
        # Create main frame with scrollbar
        self.create_scrollable_frame()
        
        # Add app header and description
        self.create_header()
        
        # Add all installation sections
        self.add_sections()
        
    def create_scrollable_frame(self):
        """Create a scrollable frame for the UI content"""
        # Create outer frame to hold canvas and scrollbar
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create canvas for scrolling
        self.canvas = tk.Canvas(frame, bg='#F4EEFF', highlightthickness=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Add vertical scrollbar
        v_scroll = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.canvas.yview)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Configure canvas scrolling
        self.canvas.configure(yscrollcommand=v_scroll.set)
        
        # Create inner frame to hold content
        self.inner_frame = tk.Frame(self.canvas, bg='#F4EEFF')
        self.inner_frame_id = self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        
        # Configure canvas and bind events
        self.inner_frame.bind("<Configure>", self.configure_canvas)
        self.canvas.bind("<Configure>", self.on_resize)
        
        # Bind mouse wheel for scrolling
        self.root.bind("<MouseWheel>", self.on_mouse_wheel)  # Windows
        self.root.bind("<Button-4>", self.on_mouse_wheel)    # Linux/macOS scroll up
        self.root.bind("<Button-5>", self.on_mouse_wheel)    # Linux/macOS scroll down
        
    def configure_canvas(self, event):
        """Update the scroll region when inner frame changes size"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def on_resize(self, event):
        """Resize the inner frame when canvas changes size"""
        canvas_width = event.width
        self.canvas.itemconfig(self.inner_frame_id, width=canvas_width)
        
    def on_mouse_wheel(self, event):
        """Handle mouse wheel scrolling"""
        if event.num == 4 or event.num == 5:  # Linux/macOS
            direction = 1 if event.num == 4 else -1
        else:  # Windows
            direction = event.delta // 120
            
        self.canvas.yview_scroll(-direction, "units")
    
    def create_header(self):
        """Create application header with logo and description"""
        # Header container
        header_frame = tk.Frame(self.inner_frame, bg='#F4EEFF')
        header_frame.pack(pady=10, fill="x")
        
        # App title
        title = tk.Label(
            header_frame,
            text="Byte Wizard",
            fg='#424874',
            bg='#F4EEFF',
            font=('Inter', 30, 'bold')
        )
        title.pack(pady=(10, 5))
        
        # App subtitle
        subtitle = tk.Label(
            header_frame,
            text="Software Installation Assistant",
            fg='#424874',
            bg='#F4EEFF',
            font=('Inter', 16)
        )
        subtitle.pack(pady=(0, 5))
        
        # App description
        description = tk.Label(
            header_frame,
            text="Quickly install essential development tools with a single click",
            fg='#6B7AA1',
            bg='#F4EEFF',
            font=('Inter', 12),
            wraplength=600
        )
        description.pack(pady=(0, 20))
    
    def add_sections(self):
        """Add all installation sections to the UI"""
        # Essential Tools Section
        self.create_section("Essential Tools", [
            ("🍫 Chocolatey", install_chocolatey, "Package manager for Windows")
        ])
        
        # Programming Languages Section
        self.create_section("Programming Languages", [
            ("🔧 C/C++ (MinGW)", install_mingw, "Compiler and tools for C/C++ development"),
            ("🐍 Python", install_python, "Popular language for scripting and applications"),
            ("☕ Java", install_java, "Cross-platform programming language")
        ])
        
        # Development Environments Section
        self.create_section("Development Environments", [
            ("📝 VS Code", install_vscode, "Lightweight and powerful code editor"),
            ("☕ NetBeans", install_netbeans, "IDE primarily for Java development"),
            ("🧠 JetBrains Tools", install_jetbrains, "Professional IDEs for various languages"),
            ("🧩 Code::Blocks", install_codeblocks, "IDE for C/C++ development")
        ])
        
        # Simulation Tools Section
        self.create_section("Simulation Tools", [
            ("📟 Iverilog", install_iverilog, "Verilog HDL simulator"),
            ("📊 GtkWave", install_gtkwave, "Waveform viewer for simulation output")
        ])
        
        # Add footer
        footer = tk.Label(
            self.inner_frame,
            text="Byte Wizard • Made with ❤️",
            fg='#6B7AA1',
            bg='#F4EEFF',
            font=('Inter', 10)
        )
        footer.pack(pady=20)
    
    def create_section(self, title, button_configs):
        """Create a section with title and buttons
        
        Args:
            title (str): Section title
            button_configs (list): List of tuples (button_text, command, tooltip)
        """
        # Section container
        section_frame = tk.Frame(self.inner_frame, bg='#F4EEFF')
        section_frame.pack(pady=10, fill="x")
        
        # Section title
        section_label = tk.Label(
            section_frame,
            text=f"  {title}",
            fg='#FFFFFF',
            bg='#424874',
            height=1,
            font=('Inter', 15, "bold"),
            anchor="w"
        )
        section_label.pack(fill="x", ipady=5)
        
        # Button container
        buttons_frame = tk.Frame(section_frame, bg='#F4EEFF', padx=15, pady=10)
        buttons_frame.pack(fill="x")
        
        # Add buttons to the section
        for i, (text, command, tooltip) in enumerate(button_configs):
            btn_frame = tk.Frame(buttons_frame, bg='#F4EEFF')
            btn_frame.grid(row=i//2, column=i%2, padx=10, pady=10, sticky="w")
            
            # Create button
            btn = tk.Button(
                btn_frame,
                text=text,
                font=("Inter", 14),
                borderwidth=0,
                highlightthickness=0,
                relief="flat",
                bg='#DCD6F7',
                fg='#424874',
                padx=15,
                pady=10,
                command=lambda cmd=command: cmd(self.root)
            )
            btn.pack(side=tk.LEFT)
            
            # Add tooltip as a label
            if tooltip:
                tooltip_label = tk.Label(
                    btn_frame,
                    text=tooltip,
                    font=("Inter", 11),
                    fg='#6B7AA1',
                    bg='#F4EEFF',
                    anchor="w"
                )
                tooltip_label.pack(side=tk.LEFT, padx=10)
            
            # Bind hover events
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave) 