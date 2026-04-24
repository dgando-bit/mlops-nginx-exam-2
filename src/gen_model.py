import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Chargement du dataset
df = pd.read_csv("data/tweet_emotions.csv")

# Séparation features / labels
X = df["content"]
y = df["sentiment"]

# Pipeline : vectorisation TF-IDF + classification
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=10000, ngram_range=(1, 2), stop_words="english")),
    ("clf", LogisticRegression(max_iter=1000, solver="lbfgs"))
])
# Entraînement
pipeline.fit(X, y)

# Sauvegarde du modèle
os.makedirs("model", exist_ok=True)
joblib.dump(pipeline, "model/model.joblib")

print("Modèle sauvegardé dans model/model.joblib")