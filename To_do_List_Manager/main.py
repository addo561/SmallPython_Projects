import streamlit as st
import pandas as pd
from xmlrpc.client import DateTime

#Class for each  task
class Task:
    def __init__(self,
        description:str,
        due_date:DateTime,
        status=False,):
            self.description = description
            self.status = status
            self.due_date = due_date
    def is_completed(self):
        return 'completed' if self.status else 'pending..'
    def edit_description(self,text:str):
        self.description = text
        return self.description


st.title('###To_do_List Manager')
