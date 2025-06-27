from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app) # Enable CORS for frontend communication

    # --- Placeholder for your actual ML Model ---
    # In a real application, you would load your trained NLP model here.
    # For example:
    # import joblib
    # model = joblib.load('path/to/your/trained_model.pkl')
    # vectorizer = joblib.load('path/to/your/tfidf_vectorizer.pkl')

def predict_fake_news(text_content):
        """
        This is a placeholder function.
        In a real scenario, this would:
        1. Preprocess the text_content (tokenization, cleaning, etc.)
        2. Use your loaded ML model to make a prediction.
        
        3. Return a classification and confidence score.
        """
        print(f"Received text for prediction: {text_content[:50]}...") # Log for debugging

        # Simulate a prediction based on keywords or random choice
        if "breaking news" in text_content.lower() and "aliens" in text_content.lower():
            return {"classification": "Fake", "confidence": 0.95}
        elif "official statement" in text_content.lower() and "government" in text_content.lower():
            return {"classification": "Real", "confidence": 0.88}
        else:
            # Randomly assign for other cases
            classifications = ["Real", "Fake", "Potentially Misleading"]
            classification = random.choice(classifications)
            confidence = round(random.uniform(0.5, 0.99), 2)
            return {"classification": classification, "confidence": confidence}



@app.route('/api/verify', methods=['POST']) # Line 39
def verify_news(): # Line 40 - MUST be at column 1
    """
    API endpoint to classify news content.
    Expects a JSON body with a 'content' field.
    """
    data = request.get_json() # Indented by 4 spaces
    if not data or 'content' not in data: # Indented by 4 spaces
        return jsonify({"error": "Missing 'content' in request body"}), 400 # Indented by 8 spaces

    text_content = data['content'] # Indented by 4 spaces
    prediction = predict_fake_news(text_content) # Indented by 4 spaces

    return jsonify({ # Indented by 4 spaces
        "status": "success", # Indented by 8 spaces
        "result": prediction # Indented by 8 spaces
    }) # Indented by 4 spaces

@app.route('/') # Line 50 - MUST be at column 1
def home(): # Line 51 - MUST be at column 1
    """Basic route to confirm backend is running.""" # Indented by 4 spaces
    return "Fake News Detector Backend is running!" # Indented by 4 spaces

if __name__ == '__main__': # Line 55 - MUST be at column 1
    # Run the Flask app
    # In production, use a WSGI server like Gunicorn (e.g., gunicorn app:app)
    app.run(debug=True, port=5000) # Indented by 4 spaces
