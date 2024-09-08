from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import tensorflow as tf
import os

# Load the model and tokenizer
model = tf.keras.models.load_model('model.keras')
vectorizer = joblib.load('tokenizer.pkl')  # Load your TfidfVectorizer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the comment from the form
        comment = request.form['comment']

        # Transform the comment using the loaded TfidfVectorizer
        comment_transformed = vectorizer.transform([comment]).toarray()

        # Predict using the loaded model
        prediction = model.predict(comment_transformed)
        prediction_class = (prediction > 0.5).astype("int32")[0][0]

        # Interpret the result
        if prediction_class == 1:
            result = "Toxic"
        else:
            result = "Non-Toxic"

        return render_template('index.html', comment=comment, prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
