import json
import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import numpy as np
import pandas as pd
from classes.clean_request import clean_request
from servises.create_df import create_df
from servises.maneg_cleaner import maneg_cleaner



app = FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        # es_handler,
        logging.FileHandler("logs/cleaner.log"),
        logging.StreamHandler()
    ]
)

@app.get("/")
def home():
    return "הכל עובד"

@app.post("/clean")
def clean(request:clean_request):
    logging.info(f"clean request, processes len:{len(request.processes.items())}")
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

        

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)


