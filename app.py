from flask import Flask, render_template, request, jsonify
import nltk
import pickle
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load the pre-trained model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Improved function to detect fake news using the trained model
def is_fake_news(text):
    # Transform the text into the format the model expects
    text_vectorized = vectorizer.transform([text])

    # Predict the class (fake or real)
    prediction = model.predict(text_vectorized)

    # Return True if fake, False if real
    return bool(prediction[0])  # Returns True (fake) or False (real)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Render index.html from templates

# Route to process fake news detection
@app.route('/detect', methods=['POST'])
def detect_fake_news():
    try:
        # Get the news text from the form data
        news_text = request.form['news_text']

        # Call the fake news detection function
        result = is_fake_news(news_text)

        # Return the result as a JSON response
        return jsonify({'is_fake': result})
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
