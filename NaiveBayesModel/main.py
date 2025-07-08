from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from NaiveBayesModel.NaiveBayes import NaiveBayes
from classes.site_info import site_info
import os

app = FastAPI()

model = NaiveBayes()
MODEL_PATH = "model.pkl"


if os.path.exists(MODEL_PATH):
    model.load(MODEL_PATH)



@app.get("/")
def home():
    return "הכל עובד"

@app.post("/fit")
def fit(data: list[site_info], labels: list[int]):
    df = pd.DataFrame([site_info.dict() for site_info in data])
    y = pd.Series(labels)
    model.fit(df, y)
    model.save(MODEL_PATH)
    return {"status": "model trained and saved"}


@app.post("/predict")
def predict(site_info: site_info):
    # df = pd.DataFrame([item.dict()])
    # pred = model.predict_row(df.iloc[0])
    # return {"prediction": int(pred)}
    return


