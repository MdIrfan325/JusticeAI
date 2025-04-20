"""
File utility module for the JusticeAI application.
Handles file operations and various format conversions.
"""

import os
import PyPDF2
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import tempfile
import re
import io
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FileUtils:
    """Utility class for handling various file operations"""
    
    @staticmethod
    def get_file_extension(file_path):
        """
        Get the extension of a file
        
        Args:
            file_path (str): Path to the file
            
        Returns:
            str: Lowercase extension without the dot
        """
        _, extension = os.path.splitext(file_path)
        return extension.lower().lstrip('.')
    
    @staticmethod
    def is_pdf(file_path):
        """
        Check if a file is a PDF
        
        Args:
            file_path (str): Path to the file
            
        Returns:
            bool: True if file is a PDF, False otherwise
        """
        return FileUtils.get_file_extension(file_path) == 'pdf'
    
    @staticmethod
    def is_image(file_path):
        """
        Check if a file is an image
        
        Args:
            file_path (str): Path to the file
            
        Returns:
            bool: True if file is an image, False otherwise
        """
        image_extensions = ['jpg', 'jpeg', 'png', 'tif', 'tiff', 'bmp']
        return FileUtils.get_file_extension(file_path) in image_extensions
    
    @staticmethod
    def validate_file(file_path):
        """
        Validate that a file exists and is of supported type
        
        Args:
            file_path (str): Path to the file
            
        Returns:
            bool: True if file is valid, False otherwise
        """
        if not os.path.isfile(file_path):
            logger.warning(f"File does not exist: {file_path}")
            return False
            
        if not (FileUtils.is_pdf(file_path) or FileUtils.is_image(file_path) or 
                FileUtils.get_file_extension(file_path) == 'txt'):
            logger.warning(f"Unsupported file type: {file_path}")
            return False
            
        return True
    
    @staticmethod
    def preprocess_image_for_ocr(image):
        """
        Preprocess image to improve OCR accuracy
        
        Args:
            image (PIL.Image): Image to preprocess
            
        Returns:
            PIL.Image: Preprocessed image
        """
        # Convert to grayscale
        image = image.convert('L')
        
        # Increase contrast
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2)
        
        # Apply slight blur to reduce noise
        image = image.filter(ImageFilter.GaussianBlur(radius=1))
        
        # Apply threshold to make text more distinct
        threshold = 150
        image = image.point(lambda p: p > threshold and 255)
        
        return image
    
    @staticmethod
    def pdf_to_images(pdf_path, dpi=300):
        """
        Convert PDF pages to images for OCR processing
        This is a more comprehensive approach than direct text extraction
        for PDFs that might contain scanned content
        
        Args:
            pdf_path (str): Path to the PDF file
            dpi (int): Resolution for the converted images
            
        Returns:
            list: List of PIL Image objects
        """
        try:
            logger.info(f"Converting PDF to images: {pdf_path}")
            
            # This function would normally use pdf2image/poppler
            # Since we're assuming those might not be available, we'll use a placeholder
            # that informs the user about the limitation
            
            return None
            
        except Exception as e:
            logger.error(f"Error converting PDF to images: {str(e)}")
            return None
    
    @staticmethod
    def read_text_file(file_path):
        """
        Read content from a text file
        
        Args:
            file_path (str): Path to the text file
            
        Returns:
            str: Content of the text file
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except UnicodeDecodeError:
            # Try with a different encoding
            try:
                with open(file_path, 'r', encoding='latin-1') as file:
                    return file.read()
            except Exception as e:
                logger.error(f"Error reading text file with latin-1 encoding: {str(e)}")
                return ""
        except Exception as e:
            logger.error(f"Error reading text file: {str(e)}")
            return ""
    
    @staticmethod
    def clean_extracted_text(text):
        """
        Clean up extracted text from OCR or PDF extraction
        
        Args:
            text (str): Text to clean
            
        Returns:
            str: Cleaned text
        """
        if not text:
            return ""
            
        # Replace multiple spaces with a single space
        text = re.sub(r'\s+', ' ', text)
        
        # Replace multiple newlines with at most two
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        # Remove strange characters often seen in OCR or PDF extraction
        text = re.sub(r'[^\x00-\x7F]+', ' ', text)
        
        return text.strip()
