#!/usr/bin/env python
# coding: utf-8

# # 판다스의 예제

# In[6]:


import pandas as pd
from time import *
df = pd.read_csv("E:\\python\\apt2021.csv", encoding="cp949")
df = df[df.지역.str.find("경기도 수원")==0]
df[:5]


# In[41]:


import pandas as pd
from time import *
df = pd.read_excel("E:\\python\\3-8.xlsx")
df["총점"]=df["국어"]+df["영어"]+df["수학"]
df["평균"]=df["총점"]/3
grade=[]
for i in df["평균"]:
    if i >= 90 :
        grade.append("A")
    elif i >= 80 :
        grade.append("B")
    elif i >= 70 :
        grade.append("C")
    elif i >= 60 :
        grade.append("D")
    else : 
        grade.append("E")
df["학점"] = grade
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




