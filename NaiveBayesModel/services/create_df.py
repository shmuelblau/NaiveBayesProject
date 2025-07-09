import pandas as pd
from io import StringIO
from classes.fit_request import fit_request
class create_df:

    @staticmethod
    def fit_df_from_request(request : fit_request):
        df = None
        if request.data_type == "json":
            df = pd.DataFrame([item.dict() for item in request.json_data]) # type: ignore

        elif request.data_type == "csv":
            df = pd.read_csv(StringIO(request.csv_data))

        elif request.data_type == "csv_path":
             df = pd.read_csv(request.csv_path)# type: ignore

        if df is not None: 
           y = df.iloc[:,-1]
           x = df.iloc[:,:-1]
           return x , y
        return None , None


    @staticmethod
    def Prediction_df_from_request(request : fit_request):
        df = None
        if request.data_type == "json":
            df = pd.DataFrame([item for item in request.json_data]) # type: ignore

        elif request.data_type == "csv":
            df = pd.read_csv(StringIO(request.csv_data))

        elif request.data_type == "csv_path":
           
            df = pd.read_csv(request.csv_path)# type: ignore
           
         

        return df
