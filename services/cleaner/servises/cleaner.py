import pandas as pd
class cleaner:

    






    @staticmethod
    def drop_duplicates(df:pd.DataFrame):
        try:
            return df.drop_duplicates()
        except:
            print("drop_null_rows: Conversion failed.")
        return df



    @staticmethod
    def drop_null_rows(df:pd.DataFrame):
        try:
            return df.dropna()
        except:
            print("drop_null_rows: Conversion failed.")
        return df
    


    @staticmethod
    def fill_null_with_mean(df: pd.DataFrame, target: str):
        try:
            if pd.api.types.is_numeric_dtype(df[target]):
                df[target] = df[target].fillna(df[target].mean())
        except:
            print("fill_null_with_mean: Conversion failed.")
        return df

    @staticmethod
    def fill_null_with_mode(df: pd.DataFrame, target: str):
        try:
            mode_val = df[target].mode()
            if not mode_val.empty:
                df[target] = df[target].fillna(mode_val[0])
        except:
            print("fill_null_with_mode: Conversion failed.")
        return df

    @staticmethod
    def fill_null_with_zeros(df: pd.DataFrame, target: str):
        try:
            df[target] = df[target].fillna(0)
        except:
            print("fill_null_with_zeros: Conversion failed.")
        return df

    @staticmethod
    def fill_null_with_ones(df: pd.DataFrame, target: str):
        try:
            df[target] = df[target].fillna(1)
        except:
            print("fill_null_with_ones: Conversion failed.")
        return df

    @staticmethod
    def convert_numeric(df: pd.DataFrame, target: str):
        try:
            df[target] = pd.to_numeric(df[target], errors='coerce')
        except:
            print("convert_numeric: Conversion failed.")
        return df

    




    @staticmethod
    def strip_strings(df: pd.DataFrame, target: str):
        try:
            df[target] = df[target].astype(str).str.strip()
        except:
            print("strip_strings: Operation failed.")
        return df

    @staticmethod
    def lowercase_strings(df: pd.DataFrame, target: str):
        try:
            df[target] = df[target].astype(str).str.lower()
        except:
            print("lowercase_strings: Operation failed.")
        return df

    @staticmethod
    def remove_special_chars(df: pd.DataFrame, target: str):
        try:
            df[target] = df[target].astype(str).str.replace(r'[^\w\s]', '', regex=True)
        except:
            print("remove_special_chars: Operation failed.")
        return df

    @staticmethod
    def standardize_dates(df: pd.DataFrame, target: str):
        try:
            df[target] = pd.to_datetime(df[target], errors='coerce')
        except:
            print("standardize_dates: Conversion failed.")
        return df

   
    @staticmethod
    def normalize_columns(df: pd.DataFrame, target: str):
        try:
            col = df[target]
            if pd.api.types.is_numeric_dtype(col):
                df[target] = (col - col.min()) / (col.max() - col.min())
        except:
            print("normalize_columns: Operation failed.")
        return df


    @staticmethod
    def remove_constant_columns(df: pd.DataFrame, target: str):
        try:
            if df[target].nunique() <= 1:
                df = df.drop(columns=[target])
        except:
            print("remove_constant_columns: Operation failed.")
        return df

    @staticmethod
    def remove_empty_columns(df: pd.DataFrame, target: str):
        try:
            if df[target].isnull().sum() / len(df) > 0.9:
                df = df.drop(columns=[target])
        except:
            print("remove_empty_columns: Operation failed.")
        return df

    @staticmethod
    def remove_long_texts(df: pd.DataFrame, target: str):
        try:
            df = df[df[target].astype(str).str.len() <= 200]
        except:
            print("remove_long_texts: Operation failed.")
        return df


    cleaning_functions = {
        "drop_duplicates": drop_duplicates.__func__,
        "drop_null_rows": drop_null_rows.__func__,
        "fill_null_with_mean": fill_null_with_mean.__func__,
        "fill_null_with_mode": fill_null_with_mode.__func__,
        "fill_null_with_zeros": fill_null_with_zeros.__func__,
        "fill_null_with_ones": fill_null_with_ones.__func__,
        "convert_numeric": convert_numeric.__func__,
        "strip_strings": strip_strings.__func__,
        "lowercase_strings": lowercase_strings.__func__,
        "remove_special_chars": remove_special_chars.__func__,
        "standardize_dates": standardize_dates.__func__,
        "normalize_columns": normalize_columns.__func__,
        "remove_constant_columns": remove_constant_columns.__func__,
        "remove_empty_columns": remove_empty_columns.__func__,
        "remove_long_texts": remove_long_texts.__func__
    }

    