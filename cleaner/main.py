import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from classes.clean_request import clean_request
from servises.create_df import create_df
from servises.maneg_cleaner import maneg_cleaner



app = FastAPI()


@app.get("/")
def home():
    return "הכל עובד"

@app.post("/clean")
def clean(request:clean_request):
    try:
        df = create_df.create_df(request)

        df = maneg_cleaner.clean_by_request(df , request)


        data = df.to_dict(orient="records")

        return JSONResponse(status_code=200,content=data)
    
    except Exception as e:
        print(e)

    return {"status":"problem in data"}

        



