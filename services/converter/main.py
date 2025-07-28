
import logging
from fastapi import FastAPI
import numpy as np
import pandas as pd


from fastapi.responses import JSONResponse
from servises import servises
from data_request import data_request

app = FastAPI()


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        # es_handler,
        logging.FileHandler("logs/converter.log"),
        logging.StreamHandler()
    ]
)



@app.get("/")
def home():
    return "הכל עובד"

@app.post("/convert")
def fit(request:data_request):
    
    logging.info(f"convert request , from type {request.data_type}")

    df = servises.df_from_request(request)

    if df is None :
        return {"status":"problem in data"}
    
   

    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.fillna(0, inplace=True)
    
    data = df.to_dict(orient="records")
    data = [{k: v for k, v in row.items() if not pd.isna(v)} for row in data]



    return JSONResponse(status_code=200,content=data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)

    
    




