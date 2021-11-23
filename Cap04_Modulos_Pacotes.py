#!/usr/bin/env python
# coding: utf-8

# # Módulos e pacotes

# In[7]:


#Assim ele importa o pacote todo
import math


# In[2]:


dir(math)


# In[3]:


math.sqrt(25)


# In[8]:


#assim eu trago somente a função especifica, economiza espaço
from math import sqrt


# In[6]:


sqrt(9)


# In[9]:


print(dir(math))


# In[10]:


help(sqrt)


# In[11]:


import random


# In[17]:


random.choice(["Maça", "Banana", "Laranja"])


# In[20]:


random.sample(range(100),10)


# In[21]:


import statistics


# In[22]:


dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]


# In[23]:


statistics.mean(dados)


# In[24]:


statistics.median(dados)


# In[25]:


import os


# In[26]:


os.getcwd()


# In[27]:


print(dir(os))


# In[28]:


import sys


# In[29]:


sys.stdout.write('Teste')


# In[30]:


sys.version


# In[31]:


print(dir(sys))


# In[32]:


import urllib.request


# In[33]:


resposta = urllib.request.urlopen('http://python.org')


# In[34]:


print(resposta)


# In[36]:


html = resposta.read()


# In[37]:


print(html)


# ## Pacote datetime

# In[1]:


import datetime


# In[ ]:





# In[2]:


agora = datetime.datetime.now()


# In[3]:


agora


# In[4]:


t = datetime.time(18, 11, 20)


# In[5]:


print(t)


# In[7]:


print("Hora: ", t.hour)
print("Minuto: ", t.minute)
print("Segundo: ", t.second)
print("Microsegundo", t.microsecond)


# In[8]:


print(datetime.time.min)


# In[9]:


hoje = datetime.date.today()


# In[10]:


print(hoje)


# In[12]:


print(hoje)
print("ctime", hoje.ctime()) #Formato completo da data
print("Dia: ", hoje.day)
print("Mês: ", hoje.month)
print("Ano:", hoje.year)


# In[13]:


d1 = datetime.date(2020, 12, 1)
print("d1: ", d1)


# In[16]:


d2 = d1.replace(year=datetime.date.today().year)


# In[15]:


print(d2)


# In[17]:


d2 - d1


# In[18]:


print(d2 - d1)


# In[ ]:




