"""
Configuration settings for the JusticeAI application.
"""

# Application metadata
APP_NAME = "JusticeAI"
APP_VERSION = "1.0.0"

# Supported file types for document upload
SUPPORTED_FILE_TYPES = (
    ("PDF files", "*.pdf"),
    ("Image files", "*.png *.jpg *.jpeg *.tif *.tiff"),
    ("All files", "*.*")
)

# NLP related configurations
SUMMARIZATION_RATIO = 0.3  # Extract 30% of original text for summaries
SIMILARITY_THRESHOLD = 0.6  # Minimum similarity score for question matching

# High-risk legal terms to highlight
HIGH_RISK_TERMS = [
    "termination", "penalty", "arbitration", "jurisdiction", "indemnity", 
    "liability", "disclaimer", "waiver", "compensation", "breach", "damages",
    "non-disclosure", "confidentiality", "severability", "prejudice",
    "forfeit", "default", "non-compete", "governing law", "damages",
    "dispute resolution", "legal fees", "suit"
]

# Medium-risk legal terms to highlight
MEDIUM_RISK_TERMS = [
    "payment", "renewal", "notice period", "assignment", "modification",
    "amendment", "force majeure", "term", "duration", "effectivity",
    "representation", "warranty", "compliance", "obligation", "responsibility"
]

# GUI related configurations
PADDING = {
    "small": 5,
    "medium": 10,
    "large": 20
}

# Font configurations
FONTS = {
    "heading1": ("Arial", 16, "bold"),
    "heading2": ("Arial", 14, "bold"),
    "heading3": ("Arial", 12, "bold"),
    "body": ("Arial", 11),
    "small": ("Arial", 9)
}

# Color scheme
COLORS = {
    "primary": "#3a0ca3",
    "secondary": "#4361ee",
    "accent": "#7209b7",
    "light_bg": "#f8f9fa",
    "dark_bg": "#e9ecef",
    "text": "#212529",
    "highlight": "#ffc107",
    "high_risk": "#dc3545",
    "medium_risk": "#fd7e14",
    "low_risk": "#20c997"
}
