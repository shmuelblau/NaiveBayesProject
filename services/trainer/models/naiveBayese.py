import numpy as np
import pandas as pd
import pickle

class NaiveBayes:
    def __init__(self):
        self._classes = []
        self._priors = {}
        self._feature_probs = {}

    
    def fit(self, X: pd.DataFrame, y: pd.Series):
        self._classes = np.unique(y)
        self._priors = {}
        self._feature_probs = {}

        for c in self._classes:
            X_c = X[y == c]
            self._priors[c] = len(X_c) / len(X)
            self._feature_probs[c] = {}

            for col in X.columns:
                value_counts = X_c[col].value_counts()
                total = len(X_c)
                k = X[col].nunique()

                self._feature_probs[c][col] = {
                    val: (value_counts.get(val, 0) + 1) / (total + k)
                    for val in X[col].unique()
                }

                


    def _predict_proba(self, X: pd.DataFrame):
        results = []
        print(111111111111111111111)
        print(self._classes)
        print(111111111111111111111)
        for _, row in X.iterrows():
            probs = {}
            for c in self._classes:
                print("222222222222222222222" + c)
                print(self._priors)
                log_prob = np.log(self._priors[c])
                for col in X.columns:
                    val = row[col]
                    prob = self._feature_probs[c][col].get(val, 1 / 1000000)
                    log_prob += np.log(prob)
                probs[c] = log_prob
            results.append(probs)
        return results

    def predict(self, X: pd.DataFrame):
        probas = self._predict_proba(X)
        return [max(p, key=p.get) for p in probas]


    def save(self, path: str):
        with open(path, "wb") as f:
            pickle.dump({
                "classes": self._classes,
                "class_priors": self._priors,
                "feature_probs": self._feature_probs
            }, f)

    def load(self, path: str):
        with open(path, "rb") as f:
            data = pickle.load(f)
            self._classes = data["classes"]
            self._priors = data["class_priors"]
            self._feature_probs = data["feature_probs"]
