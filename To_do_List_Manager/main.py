import streamlit as st
import pandas as pd 
from xmlrpc.client import DateTime

#Class for each  task 
class Task:
    def __init__(self,
        description:str,
        status:str,
        due_date:DateTime):
            return {'Description':description,'Status':status,'Due_date':due_date}

st.     