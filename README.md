# Malicious Content Detection Web App

This project is a Flask-based web application that detects and classifies toxic comments using a machine learning model. The application allows users to create, update, and delete rules that help classify text as "toxic" or "non-toxic" based on predefined rule types (keywords, phrases, contextual). It also supports managing reports (toxic content) and includes functionality for updating the reports after rules are modified.

Features
Create, update, and delete rules: Define rules using "keywords", "phrases", or "contextual text".
Text classification: Automatically classify user reports (comments) based on predefined rules and a machine learning model.
Real-time updates: When rules are updated, associated reports are re-evaluated using both the rules and the machine learning model.
Machine Learning Model: Integrated with a TensorFlow model using TF-IDF vectorization for text classification.
