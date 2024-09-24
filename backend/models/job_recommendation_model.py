from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Sample training data (resumes and job categories)
data = [
    ("Python, machine learning, deep learning", "AI Engineer"),
    ("JavaScript, React, web development", "Frontend Developer"),
    ("Linux, networking, cloud services", "DevOps Engineer"),
    ("Sales, CRM, negotiation", "Sales Manager")
]

# Split data into text (resumes) and labels (job categories)
resumes, job_categories = zip(*data)

# Convert the text data into a bag of words
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(resumes)

# Create a Naive Bayes classifier model
model = MultinomialNB()
model.fit(X, job_categories)

# Save the trained model and vectorizer
joblib.dump(model, "backend/models/job_recommendation_model.pkl")
joblib.dump(vectorizer, "backend/models/vectorizer.pkl")
