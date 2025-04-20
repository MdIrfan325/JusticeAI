"""
Question answering module for the JusticeAI application.
Matches user questions to pre-defined legal FAQs.
"""

import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Local imports
from config import SIMILARITY_THRESHOLD
from data.legal_faq import LEGAL_FAQ_CATEGORIES

def get_answer_for_question(question, category=None):
    """
    Find the best matching answer for a given question
    
    Args:
        question (str): The user's question
        category (str, optional): Specific category to search within
        
    Returns:
        dict: Result containing matching answer and related information
    """
    # Clean the question
    clean_question = _clean_text(question)
    
    # Get all questions and answers
    all_qa_pairs = _get_qa_pairs(category)
    
    if not all_qa_pairs:
        return {
            "question": question,
            "found": False,
            "similar_questions": []
        }
    
    # Get all questions for vectorization
    all_questions = [qa["question"] for qa in all_qa_pairs]
    
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer(stop_words='english')
    
    try:
        # Fit and transform the questions
        question_vectors = vectorizer.fit_transform(all_questions)
        
        # Transform the user's question
        user_question_vector = vectorizer.transform([clean_question])
        
        # Calculate similarity with all questions
        similarities = cosine_similarity(user_question_vector, question_vectors)[0]
        
        # Find the best match
        best_match_idx = similarities.argmax()
        best_match_similarity = similarities[best_match_idx]
        
        # Check if similarity is above threshold
        if best_match_similarity >= SIMILARITY_THRESHOLD:
            best_qa = all_qa_pairs[best_match_idx]
            
            # Get similar questions (excluding the best match)
            similar_questions = _get_similar_questions(similarities, all_qa_pairs, best_match_idx)
            
            return {
                "question": best_qa["question"],
                "answer": best_qa["answer"],
                "category": best_qa.get("category"),
                "similarity": best_match_similarity,
                "found": True,
                "similar_questions": similar_questions
            }
        else:
            # No good match found, return the most similar questions
            similar_indices = similarities.argsort()[-3:][::-1]  # Top 3 most similar
            similar_questions = [all_qa_pairs[i]["question"] for i in similar_indices 
                               if similarities[i] > 0.3]  # Only include somewhat similar questions
            
            return {
                "question": question,
                "found": False,
                "similar_questions": similar_questions
            }
            
    except Exception as e:
        # Handle vectorization errors (e.g., empty input)
        return {
            "question": question,
            "found": False,
            "error": str(e),
            "similar_questions": []
        }

def _clean_text(text):
    """
    Clean text for better matching
    
    Args:
        text (str): Text to clean
        
    Returns:
        str: Cleaned text
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation except question marks (these can be important)
    text = re.sub(r'[^\w\s\?]', '', text)
    
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

def _get_qa_pairs(category=None):
    """
    Get question-answer pairs, optionally filtered by category
    
    Args:
        category (str, optional): Category to filter by
        
    Returns:
        list: List of question-answer dictionaries
    """
    qa_pairs = []
    
    # If category specified, only get Q&A from that category
    if category and category in LEGAL_FAQ_CATEGORIES:
        questions = LEGAL_FAQ_CATEGORIES[category]
        for question, answer in questions.items():
            qa_pairs.append({
                "question": question,
                "answer": answer,
                "category": category
            })
    else:
        # Get Q&A from all categories
        for category, questions in LEGAL_FAQ_CATEGORIES.items():
            for question, answer in questions.items():
                qa_pairs.append({
                    "question": question,
                    "answer": answer,
                    "category": category
                })
    
    return qa_pairs

def _get_similar_questions(similarities, qa_pairs, best_match_idx, max_questions=3, min_similarity=0.5):
    """
    Get similar questions based on similarity scores
    
    Args:
        similarities (array): Array of similarity scores
        qa_pairs (list): List of question-answer dictionaries
        best_match_idx (int): Index of the best match to exclude
        max_questions (int): Maximum number of similar questions to return
        min_similarity (float): Minimum similarity threshold
        
    Returns:
        list: List of similar questions
    """
    # Get indices of top similar questions
    similar_indices = similarities.argsort()[-(max_questions+1):][::-1]
    
    # Filter out the best match and questions below the similarity threshold
    similar_questions = []
    for idx in similar_indices:
        if idx != best_match_idx and similarities[idx] >= min_similarity:
            similar_questions.append(qa_pairs[idx]["question"])
    
    return similar_questions
