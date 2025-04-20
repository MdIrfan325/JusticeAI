#!/usr/bin/env python3
"""
JusticeAI - A desktop application that helps Indian users understand legal documents 
and answer legal questions using offline NLP techniques.
"""

import os
import sys
import tkinter as tk
from tkinter import messagebox
import traceback

# Add the current directory to path to ensure imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Local imports
from gui.main_window import MainWindow
from config import APP_NAME, APP_VERSION

def handle_exception(exc_type, exc_value, exc_traceback):
    """Global exception handler to prevent app from crashing silently"""
    error_msg = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    messagebox.showerror("Error", f"An unexpected error occurred:\n{error_msg}")
    return True

def main():
    """Initialize and start the application"""
    # Set up global exception handler
    sys.excepthook = handle_exception
    
    # Create the main window
    root = tk.Tk()
    root.title(f"{APP_NAME} v{APP_VERSION}")
    root.geometry("1000x700")
    root.minsize(800, 600)
    
    # Initialize main application
    app = MainWindow(root)
    
    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()
