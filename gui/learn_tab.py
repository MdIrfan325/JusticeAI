"""
Learn Tab module for the JusticeAI application.
Contains the interface for learning about legal terms.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext

# Local imports
from config import COLORS, FONTS, PADDING
from data.legal_terms import LEGAL_TERMS, TERM_CATEGORIES

class LearnTab(ttk.Frame):
    """Tab for learning legal terms and concepts"""
    
    def __init__(self, parent):
        """Initialize the learn tab"""
        super().__init__(parent)
        
        # Create UI components
        self.create_widgets()
        
    def create_widgets(self):
        """Create UI components for the learn tab"""
        # Top section - Heading and search
        top_frame = ttk.Frame(self)
        top_frame.pack(fill=tk.X, pady=PADDING["medium"])
        
        # Heading
        ttk.Label(top_frame, text="Learn Indian Legal Terms", style="Heading.TLabel").pack(anchor=tk.W)
        ttk.Label(top_frame, text="Browse and search common legal terms and concepts used in Indian law").pack(anchor=tk.W)
        
        # Search and filter area
        search_frame = ttk.Frame(top_frame)
        search_frame.pack(fill=tk.X, pady=PADDING["medium"])
        
        # Search entry
        ttk.Label(search_frame, text="Search:").pack(side=tk.LEFT, padx=(0, PADDING["small"]))
        
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.on_search_changed)
        
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=30)
        search_entry.pack(side=tk.LEFT, padx=(0, PADDING["medium"]))
        
        # Category filter
        ttk.Label(search_frame, text="Category:").pack(side=tk.LEFT, padx=(0, PADDING["small"]))
        
        self.category_var = tk.StringVar()
        self.category_var.set("All Categories")
        self.category_var.trace("w", self.on_category_changed)
        
        category_options = ["All Categories"] + list(TERM_CATEGORIES)
        category_dropdown = ttk.Combobox(search_frame, textvariable=self.category_var, 
                                         values=category_options, state="readonly", width=20)
        category_dropdown.pack(side=tk.LEFT)
        
        # Middle section - Split view with terms list and details
        split_frame = ttk.Frame(self)
        split_frame.pack(fill=tk.BOTH, expand=True, pady=PADDING["small"])
        
        # Configure weight for resizing
        split_frame.columnconfigure(0, weight=1)
        split_frame.columnconfigure(1, weight=3)
        split_frame.rowconfigure(0, weight=1)
        
        # Left side - Terms list
        terms_frame = ttk.LabelFrame(split_frame, text="Legal Terms")
        terms_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=(0, PADDING["small"]))
        
        # Scrollable list of terms
        self.terms_listbox = tk.Listbox(terms_frame, exportselection=0, 
                                        font=FONTS["body"], activestyle='none')
        self.terms_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        terms_scrollbar = ttk.Scrollbar(terms_frame, orient=tk.VERTICAL, 
                                       command=self.terms_listbox.yview)
        terms_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.terms_listbox.config(yscrollcommand=terms_scrollbar.set)
        
        # Bind selection event
        self.terms_listbox.bind('<<ListboxSelect>>', self.on_term_selected)
        
        # Right side - Term details
        details_frame = ttk.LabelFrame(split_frame, text="Term Details")
        details_frame.grid(row=0, column=1, sticky=tk.NSEW)
        
        # Term detail widgets
        self.term_header = ttk.Label(details_frame, text="Select a term", 
                                    style="Heading.TLabel")
        self.term_header.pack(anchor=tk.W, padx=PADDING["medium"], pady=PADDING["small"])
        
        self.term_category = ttk.Label(details_frame, text="")
        self.term_category.pack(anchor=tk.W, padx=PADDING["medium"], pady=(0, PADDING["small"]))
        
        # Definition section
        definition_frame = ttk.LabelFrame(details_frame, text="Definition")
        definition_frame.pack(fill=tk.X, expand=False, padx=PADDING["medium"], 
                             pady=PADDING["small"])
        
        self.definition_text = scrolledtext.ScrolledText(
            definition_frame, wrap=tk.WORD, font=FONTS["body"], height=4)
        self.definition_text.pack(fill=tk.X, expand=True, padx=PADDING["small"], 
                                 pady=PADDING["small"])
        self.definition_text.config(state=tk.DISABLED)
        
        # Example section
        example_frame = ttk.LabelFrame(details_frame, text="Example Clause")
        example_frame.pack(fill=tk.X, expand=False, padx=PADDING["medium"], 
                          pady=PADDING["small"])
        
        self.example_text = scrolledtext.ScrolledText(
            example_frame, wrap=tk.WORD, font=FONTS["body"], height=5)
        self.example_text.pack(fill=tk.X, expand=True, padx=PADDING["small"], 
                              pady=PADDING["small"])
        self.example_text.config(state=tk.DISABLED)
        
        # Indian context section
        context_frame = ttk.LabelFrame(details_frame, text="Indian Law Context")
        context_frame.pack(fill=tk.BOTH, expand=True, padx=PADDING["medium"], 
                          pady=PADDING["small"])
        
        self.context_text = scrolledtext.ScrolledText(
            context_frame, wrap=tk.WORD, font=FONTS["body"])
        self.context_text.pack(fill=tk.BOTH, expand=True, padx=PADDING["small"], 
                              pady=PADDING["small"])
        self.context_text.config(state=tk.DISABLED)
        
        # Populate the terms list
        self.populate_terms_list()
    
    def populate_terms_list(self, search_term=None, category=None):
        """Populate the terms list based on search and filter criteria"""
        self.terms_listbox.delete(0, tk.END)
        
        # Filter terms based on search and category
        filtered_terms = []
        for term, details in LEGAL_TERMS.items():
            # Apply category filter if specified
            if category and category != "All Categories" and details["category"] != category:
                continue
                
            # Apply search filter if specified
            if search_term and search_term.lower() not in term.lower():
                continue
                
            filtered_terms.append(term)
        
        # Sort terms alphabetically
        filtered_terms.sort()
        
        # Add to listbox
        for term in filtered_terms:
            self.terms_listbox.insert(tk.END, term)
    
    def on_term_selected(self, event=None):
        """Handle selection of a term from the list"""
        selection = self.terms_listbox.curselection()
        if not selection:
            return
        
        # Get selected term
        term = self.terms_listbox.get(selection[0])
        term_data = LEGAL_TERMS.get(term)
        
        if not term_data:
            return
        
        # Update UI with term details
        self.term_header.config(text=term)
        self.term_category.config(text=f"Category: {term_data['category']}")
        
        # Update definition
        self.update_text_widget(self.definition_text, term_data.get("definition", ""))
        
        # Update example
        self.update_text_widget(self.example_text, term_data.get("example", ""))
        
        # Update Indian context
        self.update_text_widget(self.context_text, term_data.get("indian_context", ""))
    
    def update_text_widget(self, widget, text):
        """Update a text widget with new content"""
        widget.config(state=tk.NORMAL)
        widget.delete(1.0, tk.END)
        widget.insert(tk.END, text)
        widget.config(state=tk.DISABLED)
    
    def on_search_changed(self, *args):
        """Handle changes to the search field"""
        search_term = self.search_var.get()
        category = self.category_var.get()
        self.populate_terms_list(search_term, category)
    
    def on_category_changed(self, *args):
        """Handle changes to the category filter"""
        search_term = self.search_var.get()
        category = self.category_var.get()
        self.populate_terms_list(search_term, category)
