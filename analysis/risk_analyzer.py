"""
Risk analyzer module for the JusticeAI application.
Identifies risky clauses and terms in legal documents.
"""

import re
from collections import defaultdict

# Local imports
from config import HIGH_RISK_TERMS, MEDIUM_RISK_TERMS

def analyze_risks(text):
    """
    Analyze risks in the given text
    
    Args:
        text (str): The text to analyze
        
    Returns:
        dict: Information about risks identified in the text
    """
    if not text or not text.strip():
        return {
            "risk_scores": {
                "overall": "Low",
                "high_risk_count": 0,
                "medium_risk_count": 0
            },
            "highlighted_text": "No text available to analyze for risks.",
            "highlight_positions": {}
        }
    
    # Find high and medium risk terms
    high_risk_matches = _find_risk_terms(text, HIGH_RISK_TERMS)
    medium_risk_matches = _find_risk_terms(text, MEDIUM_RISK_TERMS)
    
    # Count occurrences
    high_risk_count = len(high_risk_matches)
    medium_risk_count = len(medium_risk_matches)
    
    # Calculate overall risk level
    overall_risk = _calculate_overall_risk(high_risk_count, medium_risk_count)
    
    # Prepare highlighted text
    highlight_positions = {
        "high": high_risk_matches,
        "medium": medium_risk_matches
    }
    
    return {
        "risk_scores": {
            "overall": overall_risk,
            "high_risk_count": high_risk_count,
            "medium_risk_count": medium_risk_count
        },
        "highlighted_text": text,
        "highlight_positions": _get_highlight_positions(text, high_risk_matches, medium_risk_matches)
    }

def _find_risk_terms(text, risk_terms):
    """
    Find occurrences of risk terms in the text
    
    Args:
        text (str): Text to search
        risk_terms (list): List of risk terms to find
        
    Returns:
        list: List of (term, match) tuples
    """
    matches = []
    
    # Convert text to lowercase for case-insensitive matching
    text_lower = text.lower()
    
    for term in risk_terms:
        # Create pattern for matching the term with word boundaries
        pattern = r'\b' + re.escape(term.lower()) + r'\b'
        
        # Find all matches
        for match in re.finditer(pattern, text_lower):
            matches.append((term, match))
    
    return matches

def _calculate_overall_risk(high_count, medium_count):
    """
    Calculate overall risk level based on term counts
    
    Args:
        high_count (int): Count of high risk terms
        medium_count (int): Count of medium risk terms
        
    Returns:
        str: Overall risk level (Low, Medium, or High)
    """
    # Thresholds for risk levels
    if high_count >= 5 or (high_count >= 3 and medium_count >= 5):
        return "High"
    elif high_count >= 2 or medium_count >= 3:
        return "Medium"
    else:
        return "Low"

def _get_highlight_positions(text, high_risk_matches, medium_risk_matches):
    """
    Get positions for highlighting risk terms
    
    Args:
        text (str): Original text
        high_risk_matches (list): List of high risk matches
        medium_risk_matches (list): List of medium risk matches
        
    Returns:
        dict: Dictionary of positions for each risk level
    """
    positions = {
        "high": [],
        "medium": []
    }
    
    # Extract positions for high risk terms
    for _, match in high_risk_matches:
        positions["high"].append((match.start(), match.end()))
    
    # Extract positions for medium risk terms
    for _, match in medium_risk_matches:
        positions["medium"].append((match.start(), match.end()))
    
    return positions
