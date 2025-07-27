import streamlit as st
import matplotlib.pyplot as plt
import requests
import pandas as pd
import os 




FIT_URL = os.getenv("FIT_URL")

PREDICT_URL = os.getenv("PREDICT_URL")

if "table_json" not in st.session_state:
    st.session_state.table_json = []
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()


col1, col2 = st.columns(2)


with col1:
   
    file_path = st.text_input("נתיב לקובץ")

    start1 = st.button("טען")
    
    if start1:

        df = pd.read_csv(file_path ,encoding="utf-8")

        table_json = df.to_dict(orient="records")

        table_json = [{k: v for k, v in row.items() if not pd.isna(v)} for row in table_json]

        st.session_state.table_json = table_json
        st.session_state.df = df



    






with col2:

    


    choice = st.radio("בחר פעולה" ,["אימון מודל" ,"חיזוי"] )

    if choice == "אימון מודל":
        model_name = st.text_input("שם מודל")
        target = st.text_input("עמודה לחיזוי")
        start = st.button("אמן")

        

       

        if start  :
            payload = {
            "name": model_name,
            "data" : st.session_state.table_json ,
            "target": target
            
            }

            response = requests.post(FIT_URL, json=payload)

            st.write(response.status_code)


    if choice == "חיזוי":
        model_name = st.text_input("שם מודל")
        
        start2 = st.button("חזה")

        

       

        if start2  :
            payload = {
            "name": model_name,
            "data" : st.session_state.table_json ,
           
            
            }

            response = requests.post(PREDICT_URL, json=payload)

            st.write("מוצג עם תוצאות" if response.status_code == 200 else "נכשל")



            st.session_state.df = pd.DataFrame(response.json())



st.write(st.session_state.df)
    




    

    




