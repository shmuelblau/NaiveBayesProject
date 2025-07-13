import pandas as pd 
from classes.clean_request import clean_request
from servises.cleaner import cleaner
class maneg_cleaner:


    @staticmethod
    def clean_by_request(df:pd.DataFrame , request : clean_request):

        for fank , coloms in request.processes:
            if len(coloms) == 0 :
                df = cleaner.cleaning_functions[fank](df)
                continue

            if coloms[0] == "all":
                coloms = df.columns.tolist()

            for col in coloms:
                df = cleaner.cleaning_functions[fank](df , col)

        return df
