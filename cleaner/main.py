import json
from fastapi import FastAPI
import os

app = FastAPI()






@app.get("/")
def home():
    return "הכל עובד"

@app.post("/fit")
def fit():
    
    
    return {"status": "model trained and saved"}


@app.post("/Prediction")
def Prediction():
   
    
    return 


