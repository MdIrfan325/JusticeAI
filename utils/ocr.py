"""
OCR module for the JusticeAI application.
Handles text extraction from images using pytesseract.
"""

import os
import pytesseract
from PIL import Image

def extract_text_from_image(image_path):
    """
    Extract text from an image using OCR
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        str: Extracted text from the image
    """
    try:
        # Open the image
        image = Image.open(image_path)
        
        # Convert image to grayscale for better OCR results
        if image.mode != 'L':
            image = image.convert('L')
        
        # Apply some basic image processing to improve OCR results
        # (this could be enhanced with more sophisticated techniques)
        
        # Perform OCR on the image
        # Configure pytesseract for better results with legal documents
        custom_config = r'--oem 3 --psm 6 -l eng'
        
        # Add additional languages if available (enable these if you have the language packs)
        # custom_config += ' -l eng+hin'  # Add Hindi language for Indian documents
        
        # Extract text
        text = pytesseract.image_to_string(image, config=custom_config)
        
        # Clean and return the extracted text
        return text.strip()
        
    except Exception as e:
        raise ValueError(f"Error extracting text from image: {str(e)}")
