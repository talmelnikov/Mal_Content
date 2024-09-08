# Malicious Content Detection Web App

This project is a Flask-based web application that detects and classifies toxic comments using a machine learning model. The application allows users to create, update, and delete rules that help classify text as "toxic" or "non-toxic" based on predefined rule types (keywords, phrases, contextual). It also supports managing reports (toxic content) and includes functionality for updating the reports after rules are modified.

# Features
* Create, update, and delete rules: Define rules using "keywords", "phrases", or "contextual text".
* Text classification: Automatically classify user reports (comments) based on predefined rules and a machine learning model.
* Real-time updates: When rules are updated, associated reports are re-evaluated using both the rules and the machine learning model.
* Machine Learning Model: Integrated with a TensorFlow model using TF-IDF vectorization for text classification.

# How to Use
* Dashboard: Once logged in, users can manage rules and reports.
* Rules Management:
* Navigate to the "Rules" section to create new rules or update and delete existing ones.
* Choose between "Keyword", "Phrase", or "Contextual" rule types to help classify text.
* Report Management:
* Submit a report (comment or text) to be classified as toxic or non-toxic.
* View and update reports based on the rule evaluation and machine learning model prediction.
* Machine Learning Model:
 The system uses predefined rules (created by the user) and a machine learning model to classify text.

# API Endpoints
GET /dashboard: View the user dashboard.
GET /rules: View all user-defined rules.
POST /create-rule: Create a new rule.
POST /update-rule/<rule_id>: Update an existing rule.
POST /delete-rule: Delete a rule.
GET /: View all reports.
POST /create-report: Create a new report (comment).
POST /update-report/<report_id>: Update an existing report.
POST /delete-report: Delete a report.


# Machine Learning Model
The model is a text classification model that uses a TF-IDF vectorizer and a simple neural network built using TensorFlow. The model was trained on toxic comment datasets, such as the Jigsaw Toxic Comment Classification Challenge dataset.

# Running the Model Notebook
Open the model.ipynb notebook in Jupyter.
Follow the steps to preprocess data, train the model, and evaluate its performance.
Once trained, export the model (model.h5) and the vectorizer (tfidf_vectorizer.pkl) and place them in the project directory.



The app uses a set of cleaning and pre-processing rules to handle text. This includes:

Lowercasing the text
Removing special characters
Expanding contractions (e.g., "can't" becomes "cannot")
Removing extra spaces
Built With
Flask - Web framework for Python
MongoDB - NoSQL database for storing rules and reports
TensorFlow - Machine learning framework for the text classification model
Jinja2 - Template engine for HTML rendering

