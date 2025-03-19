# PaisaBot - AI-Driven Financial Analysis & Fraud Detection

PaisaBot is an AI-powered financial analysis tool designed to analyze market trends, detect fraud in real-time, and provide automated financial analytics via an NLP-powered chatbot.

## Features
- **Real-Time Financial News Analysis**: Uses NLP to extract insights from financial news.
- **Fraud Detection with AI**: Implements OpenAI embeddings & FAISS to detect fraudulent transactions.
- **AI Chatbot for Financial Analytics**: Provides automated risk assessment and market insights.
- **Secure API Communication**: Ensures safe data transmission with HTTPS & authentication.

## Tech Stack
- **Backend**: Python, Flask
- **Frontend**: Streamlit (optional)
- **AI Models**: OpenAI GPT, FAISS (Facebook AI Similarity Search)
- **Database**: SQLite (or any preferred database)
- **Security**: HTTPS, API key authentication

## Installation
### Prerequisites
- Python 3.8+
- OpenAI API Key
- Required dependencies

### Install Required Libraries
```bash
pip install openai faiss-cpu flask pandas numpy scikit-learn streamlit
```

### Set Up OpenAI API Key
Create an environment variable for your API key:
```python
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
```

## Project Structure
```
fraud-detection-system/
├── backend/               # Flask backend and API
│   ├── app.py             # Main Flask application
│   ├── models/            # AI models and utilities
│   └── requirements.txt   # Python dependencies
├── frontend/              # Streamlit frontend (optional)
│   ├── public/            # Static assets
│   ├── src/               # React components (if needed)
│   └── package.json       # Node.js dependencies
├── ai_models/             # AI model scripts
│   ├── age_gender_detection.py  # Age and gender detection using DeepFace
│   └── fraud_detection.py       # Fraud detection using IsolationForest
└── README.md              # Project documentation
```

## Step 1: Financial News Analysis with NLP
```python
import openai

def analyze_financial_news(news_text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a financial analyst. Analyze the following news and provide insights on market trends."},
            {"role": "user", "content": news_text}
        ]
    )
    return response['choices'][0]['message']['content']
```

## Step 2: Fraud Detection with OpenAI Embeddings & FAISS
```python
import openai
import numpy as np
import faiss

def get_embedding(text):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response['data'][0]['embedding']

def detect_anomalies(embeddings, threshold=1.0):
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    distances, _ = index.search(embeddings, k=1)
    anomalies = [i for i, dist in enumerate(distances) if dist > threshold]
    return anomalies
```

## Step 3: AI-Powered Financial Chatbot
```python
def financial_chatbot(query):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a financial assistant. Provide accurate and concise answers to financial queries."},
            {"role": "user", "content": query}
        ]
    )
    return response['choices'][0]['message']['content']
```

## Step 4: API Development with Flask
```python
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/analyze_news', methods=['POST'])
def analyze_news():
    try:
        data = request.json
        news_text = data.get('news_text')
        result = analyze_financial_news(news_text)
        return jsonify({"analysis": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
```

## Step 5: Frontend with Streamlit
```python
import streamlit as st

st.title("PaisaBot - Financial Analysis Tool")

st.header("Financial News Analysis")
news_text = st.text_area("Enter financial news:")
if st.button("Analyze"):
    analysis = analyze_financial_news(news_text)
    st.write(analysis)

st.header("Financial Chatbot")
query = st.text_input("Ask a financial question:")
if st.button("Get Answer"):
    response = financial_chatbot(query)
    st.write(response)
```

## Step 6: Deployment
- **Flask API**: Deploy using AWS, GCP, or Heroku.
- **Streamlit App**: Deploy via Streamlit Sharing.
- **Security**: Use HTTPS and authentication for secure data transmission.

## Usage
1. Run the backend API:
```bash
cd backend
python app.py
```
2. Run the frontend Streamlit app:
```bash
streamlit run frontend/app.py
```

## Conclusion
PaisaBot provides a powerful, AI-driven approach to financial analysis, fraud detection, and market insights using state-of-the-art NLP techniques. 🚀

