import numpy as np
import pandas as pd
import pickle

class NaiveBayes:
    def __init__(self):
        self.classes = []
        self.class_priors = {}
        self.feature_probs = {}

    def fit(self, X: pd.DataFrame, y: pd.Series):
        self.classes = np.unique(y)
        self.class_priors = {}
        self.feature_probs = {}

        for c in self.classes:
            X_c = X[y == c]
            self.class_priors[c] = len(X_c) / len(X)
            self.feature_probs[c] = (X_c.sum(axis=0) + 1) / (len(X_c) + 2)

    def predict_proba(self, X: pd.DataFrame):
        result = []
        for _, x in X.iterrows():
            probs = {}
            for c in self.classes:
                log_prob = np.log(self.class_priors[c])
                log_prob += (x * np.log(self.feature_probs[c]) +
                             (1 - x) * np.log(1 - self.feature_probs[c])).sum()
                probs[c] = log_prob
            result.append(probs)
        return result

    def predict(self, X: pd.DataFrame):
        probas = self.predict_proba(X)
        return [max(p, key=p.get) for p in probas]

    def save(self, path: str):
        with open(path, "wb") as f:
            pickle.dump({
                "classes": self.classes,
                "class_priors": self.class_priors,
                "feature_probs": self.feature_probs
            }, f)

    def load(self, path: str):
        with open(path, "rb") as f:
            data = pickle.load(f)
            self.classes = data["classes"]
            self.class_priors = data["class_priors"]
            self.feature_probs = data["feature_probs"]
