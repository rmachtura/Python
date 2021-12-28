#!/usr/bin/env python
# coding: utf-8

# # SQLite

# In[2]:


import os
os.remove('escola.db') if os.path.exists('escola.db') else None


# In[3]:


import sqlite3


# In[4]:


con = sqlite3.connect('escola.db')


# In[5]:


type(con)


# In[6]:


cur = con.cursor()


# In[7]:


type(cur)


# In[8]:


sql_create = 'create table cursos''(id integer primary key, ''titulo varchar(100), ''categoria varchar(140))'


# In[9]:


cur.execute(sql_create)


# In[10]:


sql_insert = 'insert into cursos values (?, ?, ?)'


# In[11]:


recset = [(1000, 'Ciência de dados', 'Data Science'),
         (1001, 'Big Data Fundamentos', "Big Data"),
         (1002, 'Python Fundamentos', "Análise de dados")]


# In[13]:


for rec in recset:
    cur.execute(sql_insert, rec)


# In[14]:


con.commit()


# In[15]:


sql_select = 'select * from cursos'


# In[16]:


cur.execute(sql_select)
dados = cur.fetchall()


# In[17]:


for linha in dados:
    print("Curso: Id: %d, Tìtulo: %s, Categoria: %s \n" % linha)


# In[20]:


recset = [(1003, 'Gestão de dados com MongoDB', 'Big Data'),
         (1004, 'R Fundamentos', "Análise de dados")]
for rec in recset:
    cur.execute(sql_insert, rec)


# In[21]:


con.commit()


# In[22]:


cur.execute('select * from cursos')


# In[23]:


recset = cur.fetchall()


# In[24]:


for rec in recset:
    print("Curso: Id: %d, Tìtulo: %s, Categoria: %s \n" % rec)


# In[25]:


con.close()


# In[ ]:




