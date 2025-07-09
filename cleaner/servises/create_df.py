 
from io import StringIO
import pandas as pd

from converter.data_request import data_request


class create_df:
        


        @staticmethod
        def Prediction_df_from_request(request : data_request):
            df = None
            if request.data_type == "json":
                df = pd.DataFrame([item.dict() for item in request.json_data]) # type: ignore

            elif request.data_type == "csv":
                df = pd.read_csv(StringIO(request.csv_data))

            elif request.data_type == "csv_path":
            
                df = pd.read_csv(request.csv_path)# type: ignore
            
                

            return df