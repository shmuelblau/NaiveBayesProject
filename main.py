import json
import os
from classes.data_request import data_request
from classes.fit_request import fit_request
from classes.prediction_request import prediction_request
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import numpy as np
import pandas as pd
from classes.clean_request import clean_request
from servises.create_df import create_df
from servises.maneg_cleaner import maneg_cleaner
from servises.converter import converter
from servises.NaiveBayes import NaiveBayes

app = FastAPI()

PATH = "data/"

model = NaiveBayes()

@app.get("/")
def home():
    return "הכל עובד"
# ===================================================================================
@app.post("/clean")
def clean(request:clean_request):
    try:
        df = create_df.create_df(request)
        

        df = maneg_cleaner.clean_by_request(df , request)
       
        
        
        data = df.to_dict(orient="records")
        data = [
                        {k: v for k, v in row.items() if not pd.isna(v)}
                        for row in data
                    ]

        return JSONResponse(status_code=200,content=data)
    
    except Exception as e:
        print(111111111111111111111111111111)
        print(e)

    return {"status":"problem in data"}
# ===================================================================================

@app.post("/convert")
def convert(request:data_request):
    print(request.data_type)
    print(request.data)

    df = converter.df_from_request(request)

    if df is None :
        return {"status":"problem in data"}
    


    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.fillna(0, inplace=True)
    
    data = df.to_dict(orient="records")
    data = [{k: v for k, v in row.items() if not pd.isna(v)} for row in data]



    return JSONResponse(status_code=200,content=data)    



# ===================================================================================

@app.post("/Prediction")
def Prediction(request:prediction_request):

    model = NaiveBayes()

    df = pd.DataFrame(request.data)
    
    if df is None:
        return {"status":"problem in data"}
    

    if os.path.exists(PATH + request.name + ".pkl"):
          model.load(PATH + request.name + ".pkl")

    else:
        return {"status":"problem in model"}
    

    result = model.predict(df)
    df["class"] = result
    
    data = df.to_dict(orient="records")
    data = [{k: v for k, v in row.items() if not pd.isna(v)} for row in data]
    return JSONResponse(status_code=200,content=data)
# ===================================================================================

@app.post("/fit")
def fit(request:fit_request):
    
    x , y  = create_df.fit_df_from_request(request)
    
    if x is None or y is None:
        return {"status":"problem in data"}

    model.fit(x, y)
    model.save("data/" + request.name + ".pkl")
    return {"status": "model trained and saved"}

# ===================================================================================


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)


