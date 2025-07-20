from fastapi import FastAPI
import pandas as pd
from models.naiveBayese import NaiveBayes
from classes.fit_request import fit_request
from models.create_df import create_df
import os

app = FastAPI()

model = NaiveBayes()
MODEL_PATH = "model.pkl"



@app.get("/")
def home():
    return "הכל עובד"

@app.post("/fit")
def fit(request:fit_request):
    
    x , y  = create_df.fit_df_from_request(request)
    
    if x is None or y is None:
        return {"status":"problem in data"}

    model.fit(x, y)
    model.save(request.name+".pkl")
    return {"status": "model trained and saved"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
