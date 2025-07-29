import streamlit as st
import matplotlib.pyplot as plt
import requests
import pandas as pd
import os 



# -------------------------------------------------------------------------------

FIT_URL = os.getenv("FIT_URL" ,"http://127.0.0.1:8000/fit")

PREDICT_URL = os.getenv("PREDICT_URL" , "http://127.0.0.1:8001/Prediction")

CLEAN_URL = os.getenv("CLEAN_URL" ,"http://cleaner:8000/clean")

CONVERT_URL = os.getenv("CLEAN_URL" ,"http://converter:8000/convert")


# -------------------------------------------------------------------------------
if "table_json" not in st.session_state:
    st.session_state.table_json = []
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()

if "processes" not in st.session_state:
    st.session_state.processes = {}
# -------------------------------------------------------------------------------

col1, col2 = st.columns(2)

# ===============================================================================
# ===============================================================================

with col1:
   
    file_path = st.text_input("נתיב לקובץ")

    start1 = st.button("טען")
    
    if start1:

        df = pd.read_csv(file_path ,encoding="utf-8")

        table_json = df.to_dict(orient="records")

        table_json = [{k: v for k, v in row.items() if not pd.isna(v)} for row in table_json]

        st.session_state.table_json = table_json
        st.session_state.df = df

        st.session_state.processes = {}



    

# =====================================================================================
# =====================================================================================





with col2:

    choice = st.radio("בחר פעולה" ,["אימון מודל" ,"חיזוי","ניקוי"] )


# =================================================================================
    if choice == "אימון מודל":
        model_name = st.text_input("שם מודל")
        target = st.text_input("עמודה לחיזוי")
        start_train = st.button("אמן")

        if start_train  :
            payload = {
            "name": model_name,
            "data" : st.session_state.table_json ,
            "target": target
            
            }

            response = requests.post(FIT_URL, json=payload)

            st.write(response.status_code)
# =============================================================================
    if choice == "חיזוי":
        model_name = st.text_input("שם מודל")
        
        start_predict = st.button("חזה")

        if start_predict  :
            payload = {
            "name": model_name,
            "data" : st.session_state.table_json ,
           
            
            }

            response = requests.post(PREDICT_URL, json=payload)

            st.write("מוצג עם תוצאות" if response.status_code == 200 else "נכשל")



            st.session_state.df = pd.DataFrame(response.json())

# =====================================================================================
    if choice == "ניקוי":

        processes_list = [
            "fill_null_with_mean",
            "fill_null_with_mode",
            "fill_null_with_zeros",
            "fill_null_with_ones",
            "convert_numeric",
            "strip_strings",
            "lowercase_strings",
            "remove_special_chars",
            "standardize_dates",
            "remove_outliers",
            "normalize_columns",
            "encode_categories",
            "remove_constant_columns",
            "remove_empty_columns",
            "remove_long_texts"
            ]
        
        if len(st.session_state.table_json) == 0:
            Columns = []
        else:
            Columns = st.session_state.table_json[0].keys()
       
       

        process = st.selectbox("שם פעולה :", processes_list)
        Columns_cselected = st.multiselect("בחר עמודות:", Columns)

        add = st.button("הוסף")
        if add:
            st.session_state.processes[process] = Columns_cselected


        start_clean = st.button("נקה")

        if start_clean:

            
            payload = {
            "processes": st.session_state.processes ,
            "data" : st.session_state.table_json 
            
            }

            response = requests.post(CLEAN_URL, json=payload)

            st.write("מוצג עם תוצאות" if response.status_code == 200 else "נכשל")


            st.session_state.table_json = response.json()
            st.session_state.df = pd.DataFrame(response.json())
        


if not st.session_state.df.empty:
   st.write(st.session_state.df)
    




    

    




