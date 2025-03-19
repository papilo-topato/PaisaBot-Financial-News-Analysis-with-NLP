from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/analyze_news', methods=['POST'])
def analyze_news():
    try:
        data = request.json
        news_text = data.get('news_text')
        if not news_text:
            return jsonify({"error": "news_text is required"}), 400
        result = analyze_financial_news(news_text)
        return jsonify({"analysis": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/detect_fraud', methods=['POST'])
def detect_fraud():
    try:
        data = request.json
        transactions = data.get('transactions')
        if not transactions:
            return jsonify({"error": "transactions are required"}), 400
        embeddings = np.array([get_cached_embedding(conn, tx) for tx in transactions])
        anomalies = detect_anomalies(embeddings)
        return jsonify({"anomalies": anomalies})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        data = request.json
        query = data.get('query')
        if not query:
            return jsonify({"error": "query is required"}), 400
        response = financial_chatbot(query)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Disable debug mode for production
