import pandas as pd
from io import StringIO
from classes.fit_request import fit_request
from classes.prediction_request import prediction_request

class create_df:

    @staticmethod
    def fit_df_from_request(request : fit_request):

        df = pd.DataFrame(request.data)

        y = df[request.target]
        x = df.drop(columns=[request.target])
        return x , y
        
       
        
        
        


    @staticmethod
    def Prediction_df_from_request(request : prediction_request):
        
        return pd.DataFrame(request.data)
