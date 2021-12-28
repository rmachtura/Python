#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlite3
import random
import datetime
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'notebook # função magica do jupyter notebook, onde ele vai exibir o gráfico aqui mesmo')

conn = sqlite3.connect('dsa.db')

c = conn.cursor()

def dados_grafico():
    c.execute('SELECT id, valor FROM produtos')
    ids = []
    valores = []
    dados = c.fetchall()
    for linha in dados:
        ids.append(linha[0])
        valores.append(linha[1])
        
    plt.bar(ids, valores) #função do matplotlib para exibir o gráfico em barras
    plt.show()


# In[3]:


dados_grafico()


# In[ ]:




