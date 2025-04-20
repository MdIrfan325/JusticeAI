"""
Question Tab module for the JusticeAI application.
Contains the interface for answering legal questions.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
import threading

# Local imports
from config import COLORS, FONTS, PADDING
from analysis.question_answering import get_answer_for_question
from data.legal_faq import LEGAL_FAQ_CATEGORIES

class QuestionTab(ttk.Frame):
    """Tab for asking legal questions"""
    
    def __init__(self, parent):
        """Initialize the question tab"""
        super().__init__(parent)
        
        # Initialize state variables
        self.is_processing = False
        
        # Create UI components
        self.create_widgets()
        
    def create_widgets(self):
        """Create UI components for the question tab"""
        # Top section - Question input
        question_frame = ttk.Frame(self)
        question_frame.pack(fill=tk.X, pady=PADDING["medium"])
        
        # Heading
        ttk.Label(question_frame, text="Ask a Legal Question", style="Heading.TLabel").pack(anchor=tk.W)
        ttk.Label(question_frame, text="Enter your question related to Indian law").pack(anchor=tk.W)
        
        # Question input area
        input_frame = ttk.Frame(question_frame)
        input_frame.pack(fill=tk.X, pady=PADDING["medium"])
        
        self.question_entry = ttk.Entry(input_frame, font=FONTS["body"], width=60)
        self.question_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, PADDING["small"]))
        self.question_entry.bind("<Return>", lambda e: self.submit_question())
        
        submit_btn = ttk.Button(input_frame, text="Submit", command=self.submit_question)
        submit_btn.pack(side=tk.LEFT)
        
        # Category selector
        category_frame = ttk.Frame(question_frame)
        category_frame.pack(fill=tk.X, pady=(0, PADDING["medium"]))
        
        ttk.Label(category_frame, text="Filter by category:").pack(side=tk.LEFT, padx=(0, PADDING["small"]))
        
        self.category_var = tk.StringVar()
        self.category_var.set("All Categories")
        
        # Create categories list with "All Categories" as first option
        categories = ["All Categories"] + list(LEGAL_FAQ_CATEGORIES.keys())
        
        category_dropdown = ttk.Combobox(category_frame, textvariable=self.category_var, 
                                        values=categories, state="readonly", width=30)
        category_dropdown.pack(side=tk.LEFT)
        category_dropdown.bind("<<ComboboxSelected>>", self.on_category_selected)
        
        # Status label
        self.status_var = tk.StringVar()
        self.status_var.set("Enter your question above")
        status_label = ttk.Label(question_frame, textvariable=self.status_var)
        status_label.pack(anchor=tk.W)
        
        # Middle section - FAQ categories
        topics_frame = ttk.LabelFrame(self, text="Common Legal Topics")
        topics_frame.pack(fill=tk.X, pady=PADDING["small"], padx=PADDING["small"])
        
        # Create buttons for common topics in a grid
        self.create_topic_buttons(topics_frame)
        
        # Bottom section - Answer area
        answer_frame = ttk.LabelFrame(self, text="Answer")
        answer_frame.pack(fill=tk.BOTH, expand=True, pady=PADDING["small"], padx=PADDING["small"])
        
        self.answer_text = scrolledtext.ScrolledText(
            answer_frame, wrap=tk.WORD, font=FONTS["body"], padx=PADDING["small"], pady=PADDING["small"])
        self.answer_text.pack(fill=tk.BOTH, expand=True)
        self.answer_text.config(state=tk.DISABLED)
        
        # Show initial instruction text
        self.update_answer_text(
            "Welcome to the Legal Question Assistant!\n\n"
            "You can ask questions about Indian law by typing in the field above "
            "or by clicking on one of the common legal topics.\n\n"
            "Example questions:\n"
            "• What are my rights as a tenant?\n"
            "• How do I file a consumer complaint?\n"
            "• What is the cooling-off period for online purchases?\n"
            "• What should I check before signing an employment contract?"
        )
    
    def create_topic_buttons(self, parent):
        """Create buttons for common legal topics"""
        topics_frame = ttk.Frame(parent)
        topics_frame.pack(fill=tk.X, padx=PADDING["small"], pady=PADDING["small"])
        
        # Create a sample of common questions from each category
        row, col = 0, 0
        max_cols = 3
        
        # Get a sample question from each category
        for category, questions in LEGAL_FAQ_CATEGORIES.items():
            if questions:
                sample_question = list(questions.keys())[0]
                button = ttk.Button(
                    topics_frame, 
                    text=f"{category}: {sample_question}",
                    command=lambda q=sample_question: self.load_question(q),
                    width=30
                )
                button.grid(row=row, column=col, padx=PADDING["small"], 
                           pady=PADDING["small"], sticky=tk.W)
                
                col += 1
                if col >= max_cols:
                    col = 0
                    row += 1
    
    def load_question(self, question):
        """Load a question into the entry field"""
        self.question_entry.delete(0, tk.END)
        self.question_entry.insert(0, question)
        self.submit_question()
    
    def submit_question(self):
        """Process the question and display the answer"""
        question = self.question_entry.get().strip()
        
        if not question:
            self.status_var.set("Please enter a question")
            return
        
        if self.is_processing:
            return
        
        self.is_processing = True
        self.status_var.set("Searching for answer...")
        self.update_answer_text("Searching for the most relevant answer...")
        
        # Get selected category (if any)
        category = None
        if self.category_var.get() != "All Categories":
            category = self.category_var.get()
        
        # Process in a separate thread
        threading.Thread(
            target=self._process_question,
            args=(question, category),
            daemon=True
        ).start()
    
    def _process_question(self, question, category=None):
        """Process question in background thread"""
        try:
            # Get answer using NLP matching
            result = get_answer_for_question(question, category)
            
            # Update UI with the result
            self.master.after(0, lambda: self.update_ui_with_result(result))
            
        except Exception as e:
            self.master.after(0, lambda: self.status_var.set(f"Error: {str(e)}"))
        finally:
            self.is_processing = False
    
    def update_ui_with_result(self, result):
        """Update UI with question answering result"""
        if result["found"]:
            self.status_var.set(f"Found answer (Similarity: {result['similarity']:.0%})")
            
            answer_text = f"Q: {result['question']}\n\n"
            answer_text += f"A: {result['answer']}\n\n"
            
            if "category" in result:
                answer_text += f"Category: {result['category']}\n"
            
            if result["similar_questions"]:
                answer_text += "\nRelated questions you might want to ask:\n"
                for q in result["similar_questions"]:
                    answer_text += f"• {q}\n"
                    
            self.update_answer_text(answer_text)
        else:
            self.status_var.set("No matching answer found")
            
            no_match_text = f"Sorry, I couldn't find a specific answer to:\n\"{result['question']}\"\n\n"
            
            if result["similar_questions"]:
                no_match_text += "You might want to try these related questions instead:\n"
                for q in result["similar_questions"]:
                    no_match_text += f"• {q}\n"
            else:
                no_match_text += ("Try rephrasing your question or check the Learn Legal Terms tab "
                                "for more information on common legal concepts.")
                
            self.update_answer_text(no_match_text)
    
    def update_answer_text(self, text):
        """Update the answer text widget"""
        self.answer_text.config(state=tk.NORMAL)
        self.answer_text.delete(1.0, tk.END)
        self.answer_text.insert(tk.END, text)
        self.answer_text.config(state=tk.DISABLED)
    
    def on_category_selected(self, event=None):
        """Handle category selection change"""
        category = self.category_var.get()
        if category == "All Categories":
            self.status_var.set("Showing all categories")
        else:
            self.status_var.set(f"Filtered to category: {category}")
