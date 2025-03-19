import streamlit as st
import requests

# Flask API URL
API_URL = "http://localhost:5000"

st.title("PaisaBot - Financial Analysis Tool")

# Financial News Analysis
st.header("Financial News Analysis")
news_text = st.text_area("Enter financial news:")
if st.button("Analyze News"):
    response = requests.post(f"{API_URL}/analyze_news", json={"news_text": news_text})
    if response.status_code == 200:
        st.write(response.json().get("analysis"))
    else:
        st.error(f"Error: {response.json().get('error')}")

# Fraud Detection
st.header("Fraud Detection")
transactions = st.text_area("Enter transactions (one per line):").split('\n')
if st.button("Detect Fraud"):
    response = requests.post(f"{API_URL}/detect_fraud", json={"transactions": transactions})
    if response.status_code == 200:
        anomalies = response.json().get("anomalies")
        st.write("Anomalous transactions:", anomalies)
    else:
        st.error(f"Error: {response.json().get('error')}")

# Chatbot
st.header("Financial Chatbot")
query = st.text_input("Ask a financial question:")
if st.button("Get Answer"):
    response = requests.post(f"{API_URL}/chatbot", json={"query": query})
    if response.status_code == 200:
        st.write(response.json().get("response"))
    else:
        st.error(f"Error: {response.json().get('error')}")
