from collections import defaultdict
import streamlit as st
import pandas as pd
import datetime as dt
from datetime import datetime

#Class for each  task
class Task:
    id=0
    def __init__(self,
        description:str,
        due_date:dt.date,
        status=False):
            self.description = description
            self.status = status
            self.due_date = due_date
            Task.id += 1
            self.id_new = Task.id
           
    def is_completed(self):
        return 'completed' if self.status else 'pending..'
    def edit_description(self,text:str):
        self.description = text
        return self.description
    def get(self):
        return  [self.id_new,self.description,self.status,self.due_date]

dictionary = defaultdict(list)

class To_do_list:
    def __init__(self,task=dictionary):
        self.task = task
    
    def add_task(self,id,description,status,date):
        self.task[id] = [description,status,date]

    def delete_task(self,id):
        del self.task[id]

    def get_all(self):
        data = [(id,li[0],li[1],li[2]) for id,li in self.task.items()]
        df = pd.DataFrame(data)
        df.columns = ['id','Task','status','date']
        return df
        
    def get_pending(self,df):
        filtered = df[df['status'].str.lower()=='pending..']
        return  filtered
        
    def  get_completed(self,df):
        filtered = df[df['status'].str.lower()=='completed']
        return  filtered
        
    def  update(self,id,value):
        if isinstance(value,str):
            self.task[id][0] = value
        elif isinstance(value,bool):
            self.task[id][1] = value
        self.task[id][2] = value






st.title('To_do_List Manager')
st.sidebar.header('INPUTS')
description = st.sidebar.text_input('Task')

