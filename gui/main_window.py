"""
Main window module for the JusticeAI application.
Defines the main window and tab structure.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# Local imports
from gui.document_tab import DocumentTab
from gui.question_tab import QuestionTab
from gui.learn_tab import LearnTab
from config import APP_NAME, COLORS, FONTS, PADDING

class MainWindow:
    """Main application window with tabbed interface"""
    
    def __init__(self, master):
        """Initialize the main window with tabs"""
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Set the application icon if needed
        # self.master.iconbitmap("path/to/icon.ico")  # Uncomment and provide path if needed
        
        # Configure the main window
        self.configure_styles()
        self.create_widgets()
        
        # Display welcome message
        self.show_welcome_message()
        
    def configure_styles(self):
        """Configure ttk styles for the application"""
        style = ttk.Style()
        
        # Configure tab style
        style.configure("TNotebook", background=COLORS["light_bg"])
        style.configure("TNotebook.Tab", background=COLORS["dark_bg"], 
                        font=FONTS["heading3"], padding=[PADDING["medium"], PADDING["small"]])
        style.map("TNotebook.Tab", background=[("selected", COLORS["primary"])],
                  foreground=[("selected", "white")])
        
        # Configure other common elements
        style.configure("TFrame", background=COLORS["light_bg"])
        style.configure("TLabel", background=COLORS["light_bg"], font=FONTS["body"])
        style.configure("TButton", font=FONTS["body"], padding=PADDING["medium"])
        
        # Custom styles
        style.configure("Heading.TLabel", font=FONTS["heading1"], foreground=COLORS["primary"])
        style.configure("Subheading.TLabel", font=FONTS["heading2"])
        
    def create_widgets(self):
        """Create the main components of the application"""
        # Create main frame
        self.main_frame = ttk.Frame(self.master)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=PADDING["medium"], pady=PADDING["medium"])
        
        # Create notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.document_tab = DocumentTab(self.notebook)
        self.question_tab = QuestionTab(self.notebook)
        self.learn_tab = LearnTab(self.notebook)
        
        # Add tabs to notebook
        self.notebook.add(self.document_tab, text="Document Analysis")
        self.notebook.add(self.question_tab, text="Ask a Question")
        self.notebook.add(self.learn_tab, text="Learn Legal Terms")
        
        # Create status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.statusbar = ttk.Label(self.main_frame, textvariable=self.status_var, 
                                   relief=tk.SUNKEN, anchor=tk.W)
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def show_welcome_message(self):
        """Display a welcome message when the application starts"""
        messagebox.showinfo(
            "Welcome to JusticeAI",
            f"Welcome to {APP_NAME}!\n\n"
            "This application helps you understand legal documents and answers "
            "basic legal questions related to Indian law.\n\n"
            "• Upload legal documents for analysis\n"
            "• Ask questions about Indian law\n"
            "• Learn about common legal terms\n\n"
            "Note: All processing happens locally on your computer."
        )
    
    def on_close(self):
        """Handle window close event"""
        if messagebox.askokcancel("Quit", "Do you want to quit the application?"):
            self.master.destroy()
            sys.exit(0)
