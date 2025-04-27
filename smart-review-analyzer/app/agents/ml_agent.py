import pickle

def load_model():
    with open("app/models/logreg_churn_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("app/models/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

def predict_churn(review_text, model, vectorizer):
    X = vectorizer.transform([review_text])
    return model.predict(X)[0]
