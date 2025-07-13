import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models.NaiveBayes import NaiveBayes
from classes.fit_request import fit_request
from classes.prediction_request import prediction_request
from services.create_df import create_df
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
def fit(request:fit_request):
    
    x , y  = create_df.fit_df_from_request(request)
    
    if x is None or y is None:
        return {"status":"problem in data"}

    model.fit(x, y)
    model.save(MODEL_PATH)
    return {"status": "model trained and saved"}


@app.post("/Prediction")
def Prediction(request:prediction_request):
    df = create_df.Prediction_df_from_request(request)
    
    if df is None:
        return {"status":"problem in data"}
    result = model.predict(df)
    df["class"] = result
    
    data = df.to_dict(orient="records")
    
    return JSONResponse(status_code=200,content=data)


