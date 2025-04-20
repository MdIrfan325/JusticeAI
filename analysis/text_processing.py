"""
Text processing module for the JusticeAI application.
Handles text preprocessing, tokenization, and feature extraction.
"""

import re
import string
import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

# Initialize NLTK resources - these will be downloaded on first run
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')

# Get English stopwords
STOPWORDS = set(stopwords.words('english'))

# Add legal-specific stopwords
LEGAL_STOPWORDS = {
    'shall', 'must', 'may', 'herein', 'thereof', 'therein', 'whereof',
    'hereinafter', 'aforesaid', 'hereto', 'hereof', 'herby', 'thereby',
    'including', 'include', 'included', 'pursuant', 'accordance'
}

# Add stopwords specific to Indian legal context
INDIAN_LEGAL_STOPWORDS = {
    'pradesh', 'vidhan', 'sabha', 'lok', 'rajya', 'sarkari', 'sarkar',
    'bharat', 'bharatiya', 'hindu', 'muslim', 'sikh', 'christian',
    'rupees', 'lakh', 'crore', 'annum', 'writ', 'honourable', 'lordship'
}

# Combine all stopwords
ALL_STOPWORDS = STOPWORDS.union(LEGAL_STOPWORDS).union(INDIAN_LEGAL_STOPWORDS)

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

def preprocess_text(text, remove_stopwords=True, lemmatize=True):
    """
    Preprocess text for NLP tasks
    
    Args:
        text (str): Input text to preprocess
        remove_stopwords (bool): Whether to remove stopwords
        lemmatize (bool): Whether to lemmatize words
        
    Returns:
        str: Preprocessed text
    """
    if not text:
        return ""
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove stopwords if requested
    if remove_stopwords:
        tokens = [token for token in tokens if token not in ALL_STOPWORDS]
    
    # Lemmatize if requested
    if lemmatize:
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Rejoin tokens
    return ' '.join(tokens)

def tokenize_sentences(text):
    """
    Split text into sentences
    
    Args:
        text (str): Input text
        
    Returns:
        list: List of sentences
    """
    if not text:
        return []
    
    # Handle special cases in legal text with abbreviations
    # Replace common abbreviations to prevent false sentence breaks
    text = re.sub(r'(Mr|Mrs|Ms|Dr|Prof|vs|etc|i\.e|e\.g)\.\s', r'\1<dot> ', text)
    
    # Split into sentences
    sentences = sent_tokenize(text)
    
    # Restore the abbreviations
    sentences = [re.sub(r'<dot>', '.', s) for s in sentences]
    
    return sentences

def extract_key_phrases(text, n=10):
    """
    Extract key phrases from text using TF-IDF
    
    Args:
        text (str): Input text
        n (int): Number of key phrases to extract
        
    Returns:
        list: List of key phrases
    """
    if not text or len(text.split()) < 5:
        return []
    
    # Tokenize into sentences
    sentences = tokenize_sentences(text)
    
    if len(sentences) < 2:
        return []
    
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 3),  # Consider unigrams, bigrams, and trigrams
        max_features=5000,
        stop_words=list(ALL_STOPWORDS)
    )
    
    try:
        # Fit and transform
        tfidf_matrix = vectorizer.fit_transform(sentences)
        
        # Get feature names
        feature_names = vectorizer.get_feature_names_out()
        
        # Sum TF-IDF scores for each term across all sentences
        tfidf_sums = np.sum(tfidf_matrix.toarray(), axis=0)
        
        # Get indices of top n terms
        top_indices = tfidf_sums.argsort()[-n:][::-1]
        
        # Get the top terms
        top_phrases = [feature_names[i] for i in top_indices]
        
        return top_phrases
    
    except ValueError as e:
        # Handle case where vectorizer fails (e.g., empty content after preprocessing)
        return []

def calculate_text_similarity(text1, text2):
    """
    Calculate cosine similarity between two texts
    
    Args:
        text1 (str): First text
        text2 (str): Second text
        
    Returns:
        float: Cosine similarity score (0-1)
    """
    if not text1 or not text2:
        return 0.0
    
    # Preprocess texts
    preprocessed_text1 = preprocess_text(text1)
    preprocessed_text2 = preprocess_text(text2)
    
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    
    try:
        # Fit and transform
        tfidf_matrix = vectorizer.fit_transform([preprocessed_text1, preprocessed_text2])
        
        # Calculate cosine similarity
        similarity = (tfidf_matrix * tfidf_matrix.T).toarray()[0, 1]
        
        return similarity
    
    except ValueError:
        # Handle case where vectorizer fails
        return 0.0

def get_document_complexity(text):
    """
    Calculate readability and complexity metrics for a document
    
    Args:
        text (str): Input text
        
    Returns:
        dict: Dictionary of complexity metrics
    """
    if not text:
        return {
            "flesch_reading_ease": 0,
            "complex_word_density": 0,
            "avg_sentence_length": 0,
            "avg_word_length": 0
        }
    
    # Tokenize text
    sentences = tokenize_sentences(text)
    words = word_tokenize(text.lower())
    
    # Filter out punctuation
    words = [word for word in words if word not in string.punctuation]
    
    if not words or not sentences:
        return {
            "flesch_reading_ease": 0,
            "complex_word_density": 0,
            "avg_sentence_length": 0,
            "avg_word_length": 0
        }
    
    # Count syllables (simplified approach)
    def count_syllables(word):
        word = word.lower()
        if len(word) <= 3:
            return 1
        
        vowels = "aeiouy"
        word = word.replace("es$", "")
        word = word.replace("ed$", "")
        
        count = 0
        prev_is_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not prev_is_vowel:
                count += 1
            prev_is_vowel = is_vowel
        
        if count == 0:
            count = 1
            
        return count
    
    # Calculate metrics
    total_syllables = sum(count_syllables(word) for word in words)
    complex_words = [word for word in words if count_syllables(word) >= 3]
    complex_word_density = len(complex_words) / len(words) if words else 0
    
    avg_sentence_length = len(words) / len(sentences) if sentences else 0
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
    
    # Flesch Reading Ease score
    flesch = 206.835 - (1.015 * avg_sentence_length) - (84.6 * (total_syllables / len(words)))
    
    # Normalize Flesch score to 0-100 range
    flesch = max(0, min(100, flesch))
    
    return {
        "flesch_reading_ease": round(flesch, 2),
        "complex_word_density": round(complex_word_density, 3),
        "avg_sentence_length": round(avg_sentence_length, 2),
        "avg_word_length": round(avg_word_length, 2)
    }

def extract_named_entities(text):
    """
    Extract named entities from text (simple rule-based approach)
    
    Args:
        text (str): Input text
        
    Returns:
        dict: Dictionary of named entities by type
    """
    entities = {
        "person": [],
        "organization": [],
        "location": [],
        "date": [],
        "monetary_value": []
    }
    
    if not text:
        return entities
    
    # Person names (simple pattern for Indian names)
    person_patterns = [
        r'Mr\.\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
        r'Mrs\.\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
        r'Ms\.\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
        r'Dr\.\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
        r'Prof\.\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
        r'Shri\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
        r'Smt\.\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)'
    ]
    
    for pattern in person_patterns:
        entities["person"].extend(re.findall(pattern, text))
    
    # Organizations
    org_patterns = [
        r'([A-Z][A-Za-z]*(?:\s+[A-Z][A-Za-z]*)+)\s+(?:Limited|Ltd|Corporation|Corp|Company|Co|Private|Pvt|LLP)',
        r'([A-Z][A-Za-z]*(?:\s+[A-Z][A-Za-z]*)+)\s+(?:University|College|Institute|School)',
        r'(?:Ministry|Department)\s+of\s+([A-Za-z]+(?:\s+[A-Za-z]+)*)'
    ]
    
    for pattern in org_patterns:
        entities["organization"].extend(re.findall(pattern, text))
    
    # Locations (simple patterns for Indian locations)
    location_patterns = [
        r'(?:in|at|from|to)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*),\s+(?:India|Delhi|Mumbai|Kolkata|Chennai|Bengaluru|Hyderabad|Pune)',
        r'(?:State of|UT of)\s+([A-Za-z]+(?:\s+[A-Za-z]+)*)'
    ]
    
    for pattern in location_patterns:
        entities["location"].extend(re.findall(pattern, text))
    
    # Dates
    date_patterns = [
        r'\d{1,2}(?:st|nd|rd|th)?\s+(?:January|February|March|April|May|June|July|August|September|October|November|December),?\s+\d{4}',
        r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?,?\s+\d{4}'
    ]
    
    for pattern in date_patterns:
        entities["date"].extend(re.findall(pattern, text))
    
    # Monetary values (Indian context - Rupees, lakhs, crores)
    money_patterns = [
        r'Rs\.?\s+\d+(?:,\d+)*(?:\.\d+)?(?:\s+(?:lakhs?|crores?|millions?|billions?))?',
        r'Rupees\s+\d+(?:,\d+)*(?:\.\d+)?(?:\s+(?:lakhs?|crores?|millions?|billions?))?',
        r'\d+(?:,\d+)*(?:\.\d+)?\s+(?:lakhs?|crores?|millions?|billions?)'
    ]
    
    for pattern in money_patterns:
        entities["monetary_value"].extend(re.findall(pattern, text))
    
    # Remove duplicates and limit results
    for entity_type in entities:
        entities[entity_type] = list(set(entities[entity_type]))[:10]  # Limit to top 10
    
    return entities
