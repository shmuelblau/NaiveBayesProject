import json
from fastapi import FastAPI
import os

from fastapi.responses import JSONResponse
from servises import servises
from data_request import data_request

app = FastAPI()






@app.get("/")
def home():
    return "הכל עובד"

@app.post("/convert")
def fit(request:data_request):
    print(request.data_type)
    print(request.data)

    df = servises.df_from_request(request)

    if df is None :
        return {"status":"problem in data"}

    
    
    data = df.to_dict(orient="records")

    return JSONResponse(status_code=200,content=data)


    
    




