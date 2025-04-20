"""
JusticeAI - A web application that helps Indian users understand legal documents 
and answer legal questions using offline NLP techniques.
"""

import os
import sys
import traceback
from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
import tempfile
from werkzeug.utils import secure_filename

# Add the current directory to path to ensure imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Local imports
from config import APP_NAME, APP_VERSION
from utils.document_processor import DocumentProcessor
from analysis.summarizer import summarize_text
from analysis.risk_analyzer import analyze_risks
from analysis.question_answering import get_answer_for_question
from data.legal_terms import LEGAL_TERMS, TERM_CATEGORIES
from data.legal_faq import LEGAL_FAQ_CATEGORIES

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size

# Custom Jinja2 filter to convert newlines to HTML breaks
@app.template_filter('nl2br')
def nl2br(value):
    if not value:
        return ''
    return value.replace('\n', '<br>')

# Initialize document processor
document_processor = DocumentProcessor()

# Define allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'tif', 'tiff', 'txt'}

def allowed_file(filename):
    """Check if the file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html', app_name=APP_NAME, app_version=APP_VERSION)

@app.route('/document_analysis', methods=['GET', 'POST'])
def document_analysis():
    """Document analysis page route"""
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        
        # If user does not select file
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            # Save the file to a temporary location
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            try:
                # Process the document
                extracted_text = document_processor.extract_text(file_path)
                
                if not extracted_text:
                    flash('Failed to extract text from document')
                    return redirect(request.url)
                
                # Generate summary
                summary = summarize_text(extracted_text)
                
                # Perform risk analysis
                risk_result = analyze_risks(extracted_text)
                
                # Store results in session
                session['extracted_text'] = extracted_text
                session['summary'] = summary
                session['risk_result'] = risk_result
                
                return redirect(url_for('document_analysis_result'))
                
            except Exception as e:
                flash(f'Error processing document: {str(e)}')
                return redirect(request.url)
            finally:
                # Clean up the temporary file
                if os.path.exists(file_path):
                    os.remove(file_path)
        
    return render_template('document_analysis.html')

@app.route('/document_analysis_result')
def document_analysis_result():
    """Document analysis results page route"""
    # Retrieve results from session
    extracted_text = session.get('extracted_text', '')
    summary = session.get('summary', '')
    risk_result = session.get('risk_result', {})
    
    return render_template(
        'document_analysis_result.html',
        extracted_text=extracted_text,
        summary=summary,
        risk_result=risk_result
    )

@app.route('/ask_question', methods=['GET', 'POST'])
def ask_question():
    """Ask a legal question page route"""
    # Get all categories
    categories = ["All Categories"] + list(LEGAL_FAQ_CATEGORIES.keys())
    
    result = None
    question = ""
    category = None
    selected_category = "All Categories"
    
    if request.method == 'POST':
        question = request.form.get('question', '').strip()
        category_selection = request.form.get('category')
        selected_category = category_selection
        
        if category_selection != "All Categories":
            category = category_selection
        
        if question:
            result = get_answer_for_question(question, category)
    
    # Get sample questions for each category
    sample_questions = []
    for cat, questions in LEGAL_FAQ_CATEGORIES.items():
        if questions:
            sample_question = list(questions.keys())[0]
            sample_questions.append({
                'category': cat,
                'question': sample_question
            })
    
    return render_template(
        'ask_question.html',
        categories=categories,
        categories_data=LEGAL_FAQ_CATEGORIES,
        sample_questions=sample_questions,
        result=result,
        question=question,
        selected_category=selected_category
    )

@app.route('/learn_terms')
def learn_terms():
    """Learn legal terms page route"""
    search_term = request.args.get('search', '').lower()
    category = request.args.get('category', 'All Categories')
    
    # Filter terms based on search and category criteria
    filtered_terms = {}
    for term, details in LEGAL_TERMS.items():
        # Apply category filter if specified
        if category != "All Categories" and details["category"] != category:
            continue
        
        # Apply search filter if specified
        if search_term and search_term not in term.lower():
            continue
        
        filtered_terms[term] = details
    
    # Sort terms alphabetically
    sorted_terms = dict(sorted(filtered_terms.items()))
    
    # Get term details if a term is selected
    selected_term = request.args.get('term')
    term_details = LEGAL_TERMS.get(selected_term, {}) if selected_term else {}
    
    return render_template(
        'learn_terms.html',
        term_categories=["All Categories"] + list(TERM_CATEGORIES),
        terms=sorted_terms,
        selected_term=selected_term,
        term_details=term_details,
        search_term=search_term,
        selected_category=category
    )

@app.errorhandler(Exception)
def handle_exception(e):
    """Global exception handler"""
    error_msg = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
    app.logger.error(f"Unhandled exception: {error_msg}")
    return render_template('error.html', error=str(e), trace=error_msg), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)