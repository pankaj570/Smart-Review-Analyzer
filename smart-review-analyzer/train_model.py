import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os

data = pd.read_csv(r'app\data\large_reviews.csv')
df = pd.DataFrame(data)

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['review_text'])
y = df['label_churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

os.makedirs("app/models", exist_ok=True)
with open("app/models/logreg_churn_model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("app/models/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
