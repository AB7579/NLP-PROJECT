import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
import joblib
from sklearn.model_selection import train_test_split

from clean import clean_text

# Load the data from the CSV file
df = pd.read_csv('/workspaces/codespaces-jupyter/data/kiswahili-labeled.csv')

# Clean the text data
df['text'] = df['text'].apply(clean_text)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['sentiment'], test_size=0.2, random_state=42)

# Define the pipeline for the model
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LinearSVC())
])

# Train the model on the training data
pipeline.fit(X_train, y_train)

# Save the model to a file
joblib.dump(pipeline, 'sentiment-analysis-model.joblib')
