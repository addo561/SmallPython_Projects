import streamlit as st
import pandas as pd
from  typing import  List
import datetime




#Class for each  task
class Task:
    def __init__(self,
        id_new:int,
        description:str,
        due_date,
        status:bool):
            self.description = description
            self.status = status
            self.due_date = due_date
            self.id_new =  id_new


    def is_completed(self):
        return 'completed' if self.status else 'pending..'
    def edit_description(self,text:str):
        self.description = text
        return self.description
    def get(self):
        return  [self.id_new,self.description,self.is_completed(),self.due_date]


class To_do_list:
    def __init__(self):
        self.task = {}

    def add_task(self,task):
        self.task[task[0]] = task[1:]

    def delete_task(self,id):
        if id in self.task:
            del self.task[id]
            return True
        return False


    def  _dict(self):
        return self.task
    def get_all(self):
        data = [(id, li[0], li[1], li[2]) for id, li in self.task.items()  if len(li)>=3]
        columns:List[str]=['Id', 'Task', 'Status', 'Date']
        df = pd.DataFrame(data, columns= columns)
        return df


    def get_pending(self,df):
        filtered = df[df['Status'].str.lower()=='pending..']
        return  filtered

    def  get_completed(self,df):
        filtered = df[df['Status'].str.lower()=='completed']
        return  filtered

    def update(self, id, field, value):
        if field == "task":
            self.task[id][0] = value
        elif field == "status":
            self.task[id][1] = value
        elif field == "date":
            self.task[id][2] = value


#Raw output
task1 = Task(1,description='washing',status=False,due_date=datetime.date(2025,5,5))
task2 = Task(2,description='bath',status=False,due_date=datetime.date(2025,5,6))
task3 = Task(3,description='clean',status=False,due_date=datetime.date(2025,5,6))
task4 = Task(4,description='eat',status=False,due_date=datetime.date(2025,5,6))
task5 = Task(5,description='play',status=False,due_date=datetime.date(2025,5,6))
lists  =  To_do_list()
lists.add_task(task1.get())
lists.add_task(task2.get())
lists.add_task(task3.get())
lists.add_task(task4.get())
lists.add_task(task5.get())
print(lists._dict())
print(lists.get_all())




#streamlit interface
st.title('To_do_List Manager')
st.sidebar.header('INPUTS')
description = st.sidebar.text_input('Task')
date = st.sidebar.date_input('Date')
id= st.sidebar.number_input('Id')
finished_c = st.sidebar.checkbox('completed')
task = Task(int(id),description=description,due_date=date,status=True if  finished_c else False)

button_view = st.sidebar.button('View')
if  button_view:
    st.header('New Task')
    st.write(task.get())

button_add = st.button('Add Task')

if 'lists' not in st.session_state:
    st.session_state.lists = To_do_list()

lists = st.session_state.lists

if button_add:
    lists.add_task(task.get())
    st.markdown(':white_check_mark: Added')

button_get  =  st.button('View all')
if button_get:
    st.write(lists.get_all())
button = st.sidebar.button('Get_pending')
if button:st.write(lists.get_pending(lists.get_all()))

button = st.sidebar.button('Get_completed')
if button:st.write(lists.get_completed(lists.get_all()))

st.sidebar.subheader('DELETE')
id = st.sidebar.text_input('Enter id to  delete')
button = st.sidebar.button('Delete')
if id and button:
        lists.delete_task(id=int(id))

st.sidebar.subheader('UPDATE')
field = st.sidebar.text_input('field',key=1).lower()
id = st.sidebar.text_input('id',key=2).lower()
value =   st.sidebar.text_input('value',key=3).lower()
buttonU = st.sidebar.button('Update')
if  field and id and buttonU:
    if not value:
        st.write('Type  replacement')
    lists.update(int(id),field,value)
    st.success('Done')
