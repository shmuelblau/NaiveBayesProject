from classes.clean_request import clean_request
import pandas as pd

class create_df:

    @staticmethod
    def create_df(request:clean_request):
        return  pd.DataFrame(request.data) 