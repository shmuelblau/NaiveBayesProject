import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
from models.NaiveBayes import NaiveBayes
from classes.prediction_request import prediction_request

import os

app = FastAPI()

model = NaiveBayes()

PATH = "/app/data/"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        # es_handler,
        logging.FileHandler("logs/prediction.log"),
        logging.StreamHandler()
    ]
)


@app.get("/")
def home():
    return "הכל עובד"




@app.post("/Prediction")
def Prediction(request:prediction_request):

    logging.info(f"Prediction request, model name:{request.name}")

    df = pd.DataFrame(request.data)
    
    if df is None:
        return {"status":"problem in data"}
    

    if os.path.exists(PATH + request.name + ".pkl"):
          model.load(PATH + request.name + ".pkl")

    else:
        return JSONResponse(status_code=401,content="problem in model")
        return {"status":"problem in model"}
    

    result = model.predict(df)
    df["class"] = result
    
    data = df.to_dict(orient="records")
    data = [{k: v for k, v in row.items() if not pd.isna(v)} for row in data]
    return JSONResponse(status_code=200,content=data)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
