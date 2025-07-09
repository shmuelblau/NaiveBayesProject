from io import StringIO
from data_request import data_request
import pandas as pd
from sqlalchemy import create_engine
class servises:

    @staticmethod
    def df_from_request(request : data_request):
        df = None
        if request.data_type == "json":
            df = pd.DataFrame([item for item in request.data]) # type: ignore

        elif request.data_type == "csv":
            df = pd.read_csv(StringIO(request.data)) # type: ignore

        elif request.data_type == "csv_path":
        
            df = pd.read_csv(request.data)# type: ignore
        
        elif request.data_type == "db_path":
            
            conn_str, table_name = request.data.split("::") # type: ignore
            engine = create_engine(conn_str)


            df = pd.read_sql(f"SELECT * FROM {table_name}", engine)

        return df