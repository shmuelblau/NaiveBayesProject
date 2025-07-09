import numpy as np
import pandas as pd
import pickle

class NaiveBayes:
    def __init__(self):
        self._classes = []
        self._class_priors = {}
        self._feature_probs = {}

    def fit(self, X: pd.DataFrame, y: pd.Series):
        self._classes = np.unique(y)
        self._class_priors = {}
        self._feature_probs = {}

        for c in self._classes:
            X_c = X[y == c]
            self._class_priors[c] = len(X_c) / len(X)
            self._feature_probs[c] = (X_c.sum(axis=0) + 1) / (len(X_c) + 2)

    def _predict_proba(self, X: pd.DataFrame):
        result = []
        for _, x in X.iterrows():
            probs = {}
            for c in self._classes:
                log_prob = np.log(self._class_priors[c])
                log_prob += (x * np.log(self._feature_probs[c]) +
                             (1 - x) * np.log(1 - self._feature_probs[c])).sum()
                probs[c] = log_prob
            result.append(probs)
        return result

    def predict(self, X: pd.DataFrame):
        probas = self._predict_proba(X)
        return [max(p, key=p.get) for p in probas]

    def save(self, path: str):
        with open(path, "wb") as f:
            pickle.dump({
                "classes": self._classes,
                "class_priors": self._class_priors,
                "feature_probs": self._feature_probs
            }, f)

    def load(self, path: str):
        with open(path, "rb") as f:
            data = pickle.load(f)
            self._classes = data["classes"]
            self._class_priors = data["class_priors"]
            self._feature_probs = data["feature_probs"]
