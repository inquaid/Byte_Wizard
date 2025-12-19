import tkinter as tk
import sys
import os

# Add the src directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the main application window
from src.ui.main_window import ByteWizardApp

def main():
    """Main entry point for the Byte Wizard application"""
    # Create the root window
    root = tk.Tk()
    
    # Initialize the application
    app = ByteWizardApp(root)
    
    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main() 