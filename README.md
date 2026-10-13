# AI-Fake News Detection System 

## Overview

The Fake News Detection System is an AI-powered natural language processing application designed to classify news articles and headlines as either genuine or fabricated with high confidence.

Instead of relying on unverified claims or superficial heuristics, the system utilizes a fine-tuned DistilBERT transformer model trained on the WELFake dataset. It evaluates semantic patterns, structural language indicators, and contextual nuances to generate real-time binary classifications alongside softmax-normalized confidence scores.

The project is structured with a clean, modular architecture separating backend processing utilities from frontend assets, deployed locally via a lightweight Flask web application.

## Key Features

* Modular Inference Engine (backend/inference.py): Manages local transformer model weights, input tokenization, and forward-pass inference execution.

* Softmax Confidence Scoring: Computes percentage-based confidence scores by applying softmax probability normalization over classification logits.

* Evaluation Framework (backend/evaluation.py): Calculates quantitative performance metrics including precision, recall, F1-score, and overall accuracy against validation splits.

* Preprocessing Pipeline (backend/preprocessing.py): Sanitizes, cleans, and merges news titles and article bodies for consistent input representation.

* Interactive Sample Generator: Dynamically provides pre-configured real and fake news article samples across multiple categories (Science, Politics, Health) for instant testing.

* Responsive Web Interface (frontend/): Modern dark-themed user interface featuring interactive category pills, real/fake type selectors, and dynamic prediction confidence bars.

## How It Works

```
               INPUT (Title & Body)
                        │
                        ▼
               ┌─────────────────┐
               │    Flask API    │
               └────────┬────────┘
                        │
                        ▼
               ┌─────────────────┐
               │ DistilBERT Model│
               │  (safetensors)  │
               └────────┬────────┘
                        │
                        ▼
               ┌─────────────────┐
               │ Classification  │
               │      Logits     │
               └────────┬────────┘
                        │
                        ▼
               ┌─────────────────┐
               │ Softmax Softmax │
               │ Confidence Calc │
               └────────┬────────┘
                        │
                        ▼
               ┌─────────────────┐
               │ Final Prediction│
               │ (Real vs. Fake) │
               └─────────────────┘

```

## Methodology & Pipeline

The project follows a structured engineering workflow from data sampling to deployment:

```
01. Data Collection & Stratified Splitting (WELFake Dataset)
        ↓
02. Text Tokenization & Tensor Formatting
        ↓
03. DistilBERT Fine-Tuning on T4 GPU
        ↓
04. Modular Backend Architecture Design
        ↓
05. Quantitative Evaluation & Generalization Testing
        ↓
06. Flask Web API Integration
        ↓
07. Interactive Frontend UI Design
        ↓
08. GitHub Version Control & Deployment

```

## Technology Stack

| **Technology** | **Purpose** | 
| Python | Core Programming Language | 
| PyTorch | Deep Learning Backend Framework | 
| Hugging Face Transformers | Tokenizers & DistilBERT Sequence Classification | 
| Scikit-Learn | Metrics Evaluation & Stratified Train-Test Splitting | 
| Pandas & NumPy | Data Handling & Array Operations | 
| Flask | Backend Web API Framework | 
| HTML5 / CSS3 / JavaScript | Frontend User Interface & Asynchronous API Integration | 
| Git / GitHub | Version Control & Repository Management | 

## Project Structure

```
Fake-News-Detection-System/
│
├── app.py                      # Main entry point for Flask web server
├── requirements.txt            # Project dependencies
├── .gitignore                  # Git ignore rules
│
├── backend/
│   ├── __init__.py
│   ├── evaluation.py           # Quantitative metrics and classification report
│   ├── inference.py            # Model loading, tokenization, and prediction logic
│   └── preprocessing.py        # Text cleaning and data formatting utilities
│
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css       # Modern dark-themed UI stylesheet
│   │   └── js/
│   │       └── script.js       # Frontend API communication & DOM handlers
│   └── templates/
│       └── index.html          # Main web application layout
│
└── saved_fake_news_model/      # Fine-tuned model directory
    ├── config.json
    ├── model.safetensors
    ├── tokenizer.json
    └── tokenizer_config.json

```

## Quantitative Evaluation Results

The model was evaluated on a held-out test split of 2,000 balanced samples (1,000 fake and 1,000 real news articles), achieving the following classification metrics:

```
               precision    recall  f1-score   support

Fake News (0)       0.98      0.98      0.98      1000
Real News (1)       0.98      0.98      0.98      1000

     accuracy                           0.98      2000
    macro avg       0.98      0.98      0.98      2000
 weighted avg       0.98      0.98      0.98      2000

```

* Overall Accuracy: 98% (0.98)

* Macro Average F1-Score: 0.98

* Weighted Average F1-Score: 0.98

## Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/Abdulla-B-Official/Fake-News-Detection-Engine-Project.git
cd Fake-News-Detection-Engine-Project

```

### 2. Create a Virtual Environment

* Windows (Command Prompt):

  ```
  python -m venv venv
  venv\Scripts\activate.bat
  
  ```

* Windows (PowerShell):

  ```
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  
  ```

* Linux / macOS:

  ```
  python3 -m venv venv
  source venv/bin/activate
  
  ```

### 3. Install Dependencies

```
pip install -r requirements.txt

```

## Running the Application

### 1. Launch the Flask Web Server

From your project root directory, run:

```
python app.py

```

Open your browser and navigate to:
👉 <http://127.0.0.1:5000/>

### 2. Test via Web Interface

Use the interactive web panel to select article types (Real or Fake), choose topic categories (Science, Politics, Health), auto-generate sample text, and verify authenticity in real time.

## Future Enhancements

* Expanded Training Corpus: Incorporate multi-domain datasets to improve generalization across sensationalized science clickbait.

* Explainable AI (XAI): Integrate attention weight visualization maps (e.g., Integrated Gradients or SHAP) to highlight which words drove the prediction.

* API Rate Limiting: Implement robust security and request throttling for production readiness.

* Containerization: Provide a Dockerfile for seamless cloud container deployment.

## Project Repository

[Fake News Detection Engine Project Repository](https://github.com/Abdulla-B-Official/Fake-News-Detection-Engine-Project)

Built with: Python · PyTorch · Hugging Face Transformers · Flask · HTML/CSS/JavaScript · Git

Detect Deception. Verify Authenticity. Automate Trust.
