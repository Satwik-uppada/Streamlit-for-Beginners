import streamlit as st  

#ANCHOR - Ml function   
def ML(df):
    try:
        st.header("ML page is displaying")
        st.dataframe(df)                                                     
    except Exception as e:
            st.warning(f"Error in ML function: {e}")