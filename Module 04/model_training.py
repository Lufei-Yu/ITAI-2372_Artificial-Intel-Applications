import re
import string
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline


def clean_text(text):
    """Remove URLs and punctuation and normalize text to lowercase."""
    text = str(text)
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text)
    return text.lower().strip()


def train_sentiment_model(csv_path="sample_data.csv",
                          model_out="sentiment_model.pkl",
                          vectorizer_out="vectorizer.pkl"):
    """Train a simple TF-IDF + Naive Bayes sentiment classifier."""
    df = pd.read_csv(csv_path)
    required = {"text", "label"}
    if not required.issubset(df.columns):
        raise ValueError("CSV must contain 'text' and 'label' columns.")

    df = df.dropna(subset=["text", "label"])
    X = df["text"].apply(clean_text)
    y = df["label"].astype(str).str.lower()

    vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1)
    X_features = vectorizer.fit_transform(X)
    classifier = MultinomialNB()
    classifier.fit(X_features, y)

    # This is a tiny teaching dataset, so reported training accuracy is illustrative only.
    predictions = classifier.predict(X_features)
    print(f"Training-set accuracy (demo dataset): {accuracy_score(y, predictions):.2f}")
    print(classification_report(y, predictions, zero_division=0))

    joblib.dump(classifier, model_out)
    joblib.dump(vectorizer, vectorizer_out)
    return classifier, vectorizer


def load_sentiment_pipeline(model_path="sentiment_model.pkl",
                            vectorizer_path="vectorizer.pkl"):
    classifier = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

    def predict_sentiment(text):
        cleaned = clean_text(text)
        if not cleaned:
            return "neutral"
        features = vectorizer.transform([cleaned])
        return str(classifier.predict(features)[0]).capitalize()

    return predict_sentiment
