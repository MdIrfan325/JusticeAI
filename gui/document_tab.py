"""
Document Tab module for the JusticeAI application.
Contains the interface for uploading and analyzing legal documents.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import os
import time

# Local imports
from config import SUPPORTED_FILE_TYPES, COLORS, FONTS, PADDING
from utils.document_processor import DocumentProcessor
from utils.ocr import extract_text_from_image
from analysis.summarizer import summarize_text
from analysis.risk_analyzer import analyze_risks

class DocumentTab(ttk.Frame):
    """Tab for document upload and analysis"""
    
    def __init__(self, parent):
        """Initialize the document tab"""
        super().__init__(parent)
        
        # Initialize document processor
        self.document_processor = DocumentProcessor()
        
        # Initialize state variables
        self.current_file = None
        self.extracted_text = ""
        self.is_processing = False
        
        # Create UI components
        self.create_widgets()
        
    def create_widgets(self):
        """Create UI components for the document tab"""
        # Top section - Document upload
        upload_frame = ttk.Frame(self)
        upload_frame.pack(fill=tk.X, pady=PADDING["medium"])
        
        # Heading
        ttk.Label(upload_frame, text="Upload Legal Document", style="Heading.TLabel").pack(anchor=tk.W)
        ttk.Label(upload_frame, text="Upload a PDF or image of a legal document for analysis").pack(anchor=tk.W)
        
        # File selection frame
        file_frame = ttk.Frame(upload_frame)
        file_frame.pack(fill=tk.X, pady=PADDING["medium"])
        
        self.file_path_var = tk.StringVar()
        file_entry = ttk.Entry(file_frame, textvariable=self.file_path_var, width=50)
        file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, PADDING["small"]))
        
        browse_btn = ttk.Button(file_frame, text="Browse", command=self.browse_file)
        browse_btn.pack(side=tk.LEFT, padx=(0, PADDING["small"]))
        
        analyze_btn = ttk.Button(file_frame, text="Analyze Document", command=self.analyze_document)
        analyze_btn.pack(side=tk.LEFT)
        
        # Progress bar (hidden by default)
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(upload_frame, variable=self.progress_var, maximum=100)
        
        # Status label
        self.status_var = tk.StringVar()
        self.status_var.set("No document loaded")
        status_label = ttk.Label(upload_frame, textvariable=self.status_var)
        status_label.pack(anchor=tk.W, pady=(PADDING["small"], 0))
        
        # Middle section - Results area
        results_frame = ttk.Frame(self)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=PADDING["medium"])
        
        # Notebook for different analysis views
        self.results_notebook = ttk.Notebook(results_frame)
        self.results_notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs for different analysis results
        self.text_tab = ttk.Frame(self.results_notebook)
        self.summary_tab = ttk.Frame(self.results_notebook)
        self.risk_tab = ttk.Frame(self.results_notebook)
        
        self.results_notebook.add(self.text_tab, text="Extracted Text")
        self.results_notebook.add(self.summary_tab, text="Document Summary")
        self.results_notebook.add(self.risk_tab, text="Risk Analysis")
        
        # Extracted text tab content
        self.extracted_text_widget = scrolledtext.ScrolledText(
            self.text_tab, wrap=tk.WORD, font=FONTS["body"])
        self.extracted_text_widget.pack(fill=tk.BOTH, expand=True)
        
        # Summary tab content
        self.summary_text_widget = scrolledtext.ScrolledText(
            self.summary_tab, wrap=tk.WORD, font=FONTS["body"])
        self.summary_text_widget.pack(fill=tk.BOTH, expand=True)
        
        # Risk analysis tab content
        risk_content_frame = ttk.Frame(self.risk_tab)
        risk_content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left side - risk overview
        risk_overview_frame = ttk.Frame(risk_content_frame)
        risk_overview_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        ttk.Label(risk_overview_frame, text="Risk Assessment", 
                 style="Subheading.TLabel").pack(anchor=tk.W, pady=PADDING["small"])
        
        self.risk_overview_text = scrolledtext.ScrolledText(
            risk_overview_frame, wrap=tk.WORD, height=5, font=FONTS["body"])
        self.risk_overview_text.pack(fill=tk.X, expand=False, pady=PADDING["small"])
        
        ttk.Label(risk_overview_frame, text="Highlighted Risky Clauses", 
                 style="Subheading.TLabel").pack(anchor=tk.W, pady=PADDING["small"])
        
        self.risk_detail_text = scrolledtext.ScrolledText(
            risk_overview_frame, wrap=tk.WORD, font=FONTS["body"])
        self.risk_detail_text.pack(fill=tk.BOTH, expand=True, pady=PADDING["small"])
        
        # Configure text tags for highlighting
        for widget in [self.extracted_text_widget, self.summary_text_widget, self.risk_detail_text]:
            widget.tag_configure("high_risk", background=COLORS["high_risk"], foreground="white")
            widget.tag_configure("medium_risk", background=COLORS["medium_risk"])
            widget.tag_configure("low_risk", background=COLORS["low_risk"])
            widget.config(state=tk.DISABLED)  # Initially disabled
        
        self.risk_overview_text.config(state=tk.DISABLED)
    
    def browse_file(self):
        """Open file dialog to select a document"""
        file_path = filedialog.askopenfilename(
            title="Select Legal Document",
            filetypes=SUPPORTED_FILE_TYPES
        )
        
        if file_path:
            self.file_path_var.set(file_path)
            self.current_file = file_path
            self.status_var.set(f"Selected: {os.path.basename(file_path)}")
    
    def analyze_document(self):
        """Process and analyze the selected document"""
        if not self.current_file:
            messagebox.showwarning("No Document", "Please select a document first.")
            return
        
        if self.is_processing:
            messagebox.showinfo("Processing", "Document analysis is already in progress.")
            return
        
        # Clear previous results
        self.clear_results()
        
        # Show progress bar
        self.progress_bar.pack(fill=tk.X, pady=PADDING["small"])
        self.is_processing = True
        
        # Start processing in a separate thread
        threading.Thread(target=self._process_document, daemon=True).start()
    
    def _process_document(self):
        """Process document in background thread"""
        try:
            self.status_var.set("Processing document...")
            self.progress_var.set(10)
            
            # Extract text from document
            self.extracted_text = self.document_processor.extract_text(self.current_file)
            self.progress_var.set(40)
            
            if not self.extracted_text:
                self.update_status("Failed to extract text from document", is_error=True)
                return
            
            # Update extracted text view
            self.update_text_widget(self.extracted_text_widget, self.extracted_text)
            self.progress_var.set(60)
            
            # Generate summary
            summary = summarize_text(self.extracted_text)
            self.update_text_widget(self.summary_text_widget, summary)
            self.progress_var.set(80)
            
            # Perform risk analysis
            risk_result = analyze_risks(self.extracted_text)
            
            # Update risk analysis view
            self.update_risk_analysis(risk_result)
            self.progress_var.set(100)
            
            # Update status
            self.update_status(f"Analysis complete: {os.path.basename(self.current_file)}")
            
        except Exception as e:
            self.update_status(f"Error: {str(e)}", is_error=True)
        finally:
            # Hide progress bar and reset state
            self.master.after(0, lambda: self.progress_bar.pack_forget())
            self.is_processing = False
    
    def update_status(self, message, is_error=False):
        """Update status message on the UI thread"""
        def _update():
            self.status_var.set(message)
            if is_error:
                messagebox.showerror("Error", message)
        
        self.master.after(0, _update)
    
    def update_text_widget(self, widget, text):
        """Update text widget on the UI thread"""
        def _update():
            widget.config(state=tk.NORMAL)
            widget.delete(1.0, tk.END)
            widget.insert(tk.END, text)
            widget.config(state=tk.DISABLED)
        
        self.master.after(0, _update)
    
    def update_risk_analysis(self, risk_result):
        """Update risk analysis widgets on the UI thread"""
        def _update():
            # Update overview
            self.risk_overview_text.config(state=tk.NORMAL)
            self.risk_overview_text.delete(1.0, tk.END)
            
            risk_scores = risk_result.get("risk_scores", {})
            overview_text = f"Overall Risk Level: {risk_scores.get('overall', 'Unknown')}\n"
            overview_text += f"High Risk Terms: {risk_scores.get('high_risk_count', 0)}\n"
            overview_text += f"Medium Risk Terms: {risk_scores.get('medium_risk_count', 0)}\n"
            
            self.risk_overview_text.insert(tk.END, overview_text)
            self.risk_overview_text.config(state=tk.DISABLED)
            
            # Update detailed view with highlighted terms
            self.risk_detail_text.config(state=tk.NORMAL)
            self.risk_detail_text.delete(1.0, tk.END)
            
            # Add highlighted text with risky terms
            highlighted_text = risk_result.get("highlighted_text", "")
            if highlighted_text:
                self.risk_detail_text.insert(tk.END, highlighted_text)
            
            # Apply highlighting based on positions
            for term_type, positions in risk_result.get("highlight_positions", {}).items():
                tag_name = f"{term_type}_risk"
                for start, end in positions:
                    self.risk_detail_text.tag_add(tag_name, f"1.{start}", f"1.{end}")
            
            self.risk_detail_text.config(state=tk.DISABLED)
        
        self.master.after(0, _update)
    
    def clear_results(self):
        """Clear all result widgets"""
        for widget in [self.extracted_text_widget, self.summary_text_widget, 
                      self.risk_detail_text, self.risk_overview_text]:
            widget.config(state=tk.NORMAL)
            widget.delete(1.0, tk.END)
            widget.config(state=tk.DISABLED)
