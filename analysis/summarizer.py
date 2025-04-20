"""
Summarizer module for the JusticeAI application.
Handles text summarization using frequency-based and extractive methods.
"""

import re
import heapq
import string
from collections import Counter

# Local imports
from config import SUMMARIZATION_RATIO

def summarize_text(text, ratio=SUMMARIZATION_RATIO):
    """
    Generate an extractive summary of the given text
    
    Args:
        text (str): The text to summarize
        ratio (float): The ratio of sentences to include in the summary
        
    Returns:
        str: The generated summary
    """
    if not text or not text.strip():
        return "No text available to summarize."
    
    # Clean the text
    clean_text = _clean_text(text)
    
    # Split into sentences
    sentences = _split_into_sentences(clean_text)
    
    if len(sentences) <= 3:
        return text  # Text is already short, return as is
    
    # Calculate sentence scores
    sentence_scores = _score_sentences(sentences)
    
    # Determine how many sentences to include in the summary
    summary_size = max(3, int(len(sentences) * ratio))
    
    # Get the highest scoring sentences
    best_sentences = heapq.nlargest(summary_size, sentence_scores, key=sentence_scores.get)
    
    # Sort sentences by their original order
    best_sentences.sort(key=lambda s: sentences.index(s))
    
    # Combine the sentences into a summary
    summary = " ".join(best_sentences)
    
    return summary

def _clean_text(text):
    """
    Clean the text for better summarization
    
    Args:
        text (str): Text to clean
        
    Returns:
        str: Cleaned text
    """
    # Replace newlines with spaces
    text = re.sub(r'\n+', ' ', text)
    
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

def _split_into_sentences(text):
    """
    Split text into sentences
    
    Args:
        text (str): Text to split
        
    Returns:
        list: List of sentences
    """
    # Simple sentence splitting by punctuation followed by space
    # This is a simplified approach; a more sophisticated one would use NLP libraries
    sentence_delimiters = r'[.!?][\s\n]'
    sentences = re.split(sentence_delimiters, text)
    
    # Filter out empty sentences and clean them
    return [s.strip() for s in sentences if s.strip()]

def _score_sentences(sentences):
    """
    Score sentences based on word frequency
    
    Args:
        sentences (list): List of sentences
        
    Returns:
        dict: Dictionary of sentences and their scores
    """
    # Flatten all sentences into a single string for word frequency analysis
    all_text = ' '.join(sentences)
    
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    all_text = all_text.translate(translator).lower()
    
    # Get word frequencies
    words = all_text.split()
    word_frequencies = Counter(words)
    
    # Calculate the maximum frequency for normalization
    max_frequency = max(word_frequencies.values()) if word_frequencies else 1
    
    # Normalize word frequencies
    for word in word_frequencies:
        word_frequencies[word] /= max_frequency
    
    # Score each sentence based on word frequencies
    sentence_scores = {}
    for sentence in sentences:
        # Skip very short sentences
        if len(sentence.split()) <= 3:
            continue
            
        # Remove punctuation and convert to lowercase for scoring
        clean_sentence = sentence.translate(translator).lower()
        words = clean_sentence.split()
        
        # Calculate sentence score as the sum of word frequencies
        score = sum(word_frequencies.get(word, 0) for word in words)
        
        # Normalize by sentence length to avoid bias towards longer sentences
        # (but with a dampening factor to still give some weight to longer sentences)
        sentence_length = max(1, len(words))
        score = score / (sentence_length ** 0.5)  # Square root dampening
        
        sentence_scores[sentence] = score
    
    return sentence_scores
