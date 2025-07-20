import pandas as pd
from classes.fit_request import fit_request


class create_df:

    @staticmethod
    def fit_df_from_request(request : fit_request):

        df = pd.DataFrame(request.data)

        y = df[request.target]
        x = df.drop(columns=[request.target])
        return x , y
        
       
        
        
        


   
