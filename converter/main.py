
from fastapi import FastAPI
import numpy as np
import pandas as pd


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
    
    print(df.head())

    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.fillna(0, inplace=True)
    
    data = df.to_dict(orient="records")
    data = [{k: v for k, v in row.items() if not pd.isna(v)} for row in data]



    return JSONResponse(status_code=200,content=data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)

    
    




