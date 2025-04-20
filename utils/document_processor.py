"""
Document processor module for the JusticeAI application.
Handles extracting text from various document formats.
"""

import os
import re
from pathlib import Path
import PyPDF2
from PIL import Image

# Local imports
from utils.ocr import extract_text_from_image

class DocumentProcessor:
    """Processes documents and extracts text content"""
    
    def __init__(self):
        """Initialize the document processor"""
        pass
    
    def extract_text(self, file_path):
        """
        Extract text from a document file
        
        Args:
            file_path (str): Path to the document file
            
        Returns:
            str: Extracted text from the document
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        file_extension = Path(file_path).suffix.lower()
        
        # Extract text based on file type
        if file_extension == '.pdf':
            return self._extract_text_from_pdf(file_path)
        elif file_extension in ['.png', '.jpg', '.jpeg', '.tif', '.tiff']:
            return extract_text_from_image(file_path)
        else:
            # Try to read as plain text
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    return file.read()
            except UnicodeDecodeError:
                try:
                    # Try with a different encoding
                    with open(file_path, 'r', encoding='latin-1') as file:
                        return file.read()
                except Exception:
                    raise ValueError(f"Unsupported file format: {file_extension}")
    
    def _extract_text_from_pdf(self, file_path):
        """
        Extract text from a PDF file
        
        Args:
            file_path (str): Path to the PDF file
            
        Returns:
            str: Extracted text from the PDF
        """
        try:
            text = ""
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                num_pages = len(pdf_reader.pages)
                
                for page_num in range(num_pages):
                    page = pdf_reader.pages[page_num]
                    page_text = page.extract_text()
                    
                    if page_text:
                        text += page_text + "\n\n"
            
            # Clean up the text
            text = self._clean_text(text)
            
            # If no text was extracted, try OCR as fallback
            if not text.strip():
                # Convert PDF to images and use OCR
                text = self._ocr_fallback_for_pdf(file_path)
            
            return text
        
        except Exception as e:
            raise ValueError(f"Error extracting text from PDF: {str(e)}")
    
    def _ocr_fallback_for_pdf(self, file_path):
        """
        Use OCR as a fallback for PDFs where text extraction fails
        
        This is a placeholder as converting PDFs to images requires additional
        libraries like pdf2image with poppler, which might not be available.
        """
        # This would require pdf2image with poppler, which might be complex for users to install
        # Instead, return a message informing the user
        return "This PDF appears to contain scanned pages or images that require OCR processing. " \
               "For better results, consider converting the PDF to images first or use an image of the document."
    
    def _clean_text(self, text):
        """
        Clean extracted text
        
        Args:
            text (str): Text to clean
            
        Returns:
            str: Cleaned text
        """
        if not text:
            return ""
        
        # Replace multiple spaces with a single space
        text = re.sub(r'\s+', ' ', text)
        
        # Replace multiple newlines with a maximum of two
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        return text.strip()
