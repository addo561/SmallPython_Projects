from collections import defaultdict 
from scipy.stats import rankdata
import pandas as pd

print('SAVE')
container = defaultdict(list)
num = int(input('Number of students: '))
courses = int(input('Courses: '))

for i in range(num):
    name = input('Name: ')
    for j in range(courses):
        score = int(input('Score: '))
        container[name].append(score)
#Grade
def grade(D):
    newD = defaultdict(list)
    for i in D:
        L = D[i]
        for j in L:
            if j >=80:
                newD[i].append('A -> Excellent')
            elif 60<j<79:
                newD[i].append('B -> Very Good')
            elif 40<j<59:
                newD[i].append('C -> Good')
            elif 29<j<39:
                newD[i].append('D -> Pass')
            else:
                newD[i].append('E-F -> Fail')                
    return newD 
#Rankings
def rank(D):
    total = defaultdict(list)
    for i in D:
        L = D[i]
        sumJ = 0
        for j in L:
            sumJ += int(j)
        total[i].append(sumJ)
    
    df = pd.DataFrame(dict(total)).T
    df.columns = ['Total_Score']
    df['Position'] = df['Total_Score'].rank(method='min',ascending=False)
    return df
  

print(container)     
print(grade(container))  
print(rank(container))      
  
    