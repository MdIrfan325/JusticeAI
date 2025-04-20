# JusticeAI - Indian Legal Assistant

JusticeAI is a web-based application designed to help Indian users understand legal documents, get answers to common legal questions, and learn about legal terms commonly used in Indian law - all completely offline with no need for external APIs.

![JusticeAI Screenshot](./generated-icon.png)

## Features

### 1. Document Analysis
- Upload legal documents (PDF, images, text files)
- Extract text from documents using OCR when needed
- Generate concise summaries of legal documents
- Identify potentially risky clauses and terms
- View full document with highlighted risk terms

### 2. Legal Question Answering
- Get answers to common legal questions about Indian law
- Filter questions by category
- View related questions for further exploration
- Responses presented in easy-to-understand bullet points

### 3. Legal Terms Learning
- Browse a comprehensive database of legal terms
- Filter terms by category or search for specific terms
- View detailed definitions, examples, and Indian law context

## Installation

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/yourusername/justiceai.git
cd justiceai
```

2. Install dependencies
```bash
pip install -r requirements.txt
```
or
```bash
pip install flask nltk pillow pypdf2 pytesseract scikit-learn
```

3. Install NLTK data (for text processing)
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

4. For OCR functionality, install Tesseract
   - For Ubuntu/Debian: `sudo apt-get install tesseract-ocr`
   - For macOS: `brew install tesseract`
   - For Windows: Download and install from [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

## Running the Application

1. Start the Flask server
```bash
python app.py
```

2. Open your web browser and go to:
```
http://localhost:5000
```

## Project Structure

```
JusticeAI/
│
├── analysis/               # NLP analysis modules
│   ├── __init__.py
│   ├── question_answering.py
│   ├── risk_analyzer.py
│   ├── summarizer.py
│   └── text_processing.py
│
├── data/                   # Static data
│   ├── __init__.py
│   ├── legal_faq.py        # Q&A database
│   └── legal_terms.py      # Legal terms database
│
├── templates/              # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── document_analysis.html
│   ├── document_analysis_result.html
│   ├── ask_question.html
│   ├── learn_terms.html
│   └── error.html
│
├── utils/                  # Utility functions
│   ├── __init__.py
│   ├── document_processor.py
│   ├── file_utils.py
│   └── ocr.py
│
├── app.py                  # Flask application
├── config.py               # Configuration settings
└── main.py                 # Command-line interface
```

## Usage Examples

### Analyzing a Document

1. Navigate to the "Document Analysis" page
2. Upload a legal document (PDF, image, or text file)
3. The system will:
   - Extract text from the document
   - Generate a summary
   - Identify potentially risky clauses
4. Review the analysis results in the three tabs:
   - Document Summary
   - Risk Analysis
   - Full Text

### Asking Legal Questions

1. Navigate to the "Ask a Question" page
2. Enter your question or select a category to browse common questions
3. Review the answer and related questions

### Learning Legal Terms

1. Navigate to the "Learn Legal Terms" page
2. Browse terms by category or search for specific terms
3. Click on a term to view its definition, example usage, and Indian context

## Deployment

### Local Deployment

To run the application in a production environment, it's recommended to use a WSGI server like Gunicorn:

1. Install Gunicorn
```bash
pip install gunicorn
```

2. Run the application with Gunicorn
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Deploying on a Server

1. Set up a server with Python installed (Ubuntu/Debian example)
```bash
sudo apt update
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools tesseract-ocr
```

2. Clone the repository and install dependencies
```bash
git clone https://github.com/yourusername/justiceai.git
cd justiceai
pip install -r requirements.txt
pip install gunicorn
```

3. Configure Nginx (optional, for reverse proxy)
```bash
sudo apt install nginx
```

4. Create an Nginx configuration file
```
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

5. Start the application with Gunicorn
```bash
gunicorn -w 4 -b 127.0.0.1:5000 app:app
```

6. For automatic startup, create a systemd service
```bash
sudo nano /etc/systemd/system/justiceai.service
```

7. Add the following configuration
```
[Unit]
Description=JusticeAI web application
After=network.target

[Service]
User=yourusername
WorkingDirectory=/path/to/justiceai
ExecStart=/usr/local/bin/gunicorn -w 4 -b 127.0.0.1:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

8. Enable and start the service
```bash
sudo systemctl enable justiceai
sudo systemctl start justiceai
```

### Deploying on Cloud Platforms

#### Heroku
1. Create a Procfile in the root directory
```
web: gunicorn app:app
```

2. Create a requirements.txt file
3. Create a runtime.txt file with your Python version
4. Deploy using Heroku CLI
```bash
heroku create justiceai
git push heroku main
```

#### AWS, Google Cloud, or Azure
Follow their respective platform documentation for deploying Flask applications.

## Limitations

- OCR functionality may not be perfect for all document types
- The legal term database and Q&A system are limited to the pre-loaded data
- No internet connection means no updates to the legal information

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This project uses natural language processing techniques for text analysis
- Legal information is sourced with a focus on Indian law
- Designed to work completely offline without any external API dependencies