#!/usr/bin/env python
# coding: utf-8

# # Insert SQLite

# In[2]:


import os
os.remove('dsa.db') if os.path.exists('dsa.db') else None


# In[5]:


import sqlite3
import random
import time
import datetime

#Criando conexao
conn = sqlite3.connect('dsa.db')

#criando um cursor
cur = conn.cursor()

#função para criar tabela
def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT,'               'prod_name TEXT, valor REAL)')
    
def data_insert():
    cur.execute("INSERT INTO produtos VALUES(NULL,'2021-12-20 19:22:00', 'Teclado', 90)")
    conn.commit()
    cur.close()
    conn.close()
    
def data_insert_var():
    new_date = datetime.datetime.now()
    product = "Monitor"
    price = random.randrange(500, 1000)
    cur.execute('INSERT INTO produtos VALUES(NULL,?, ?, ?)', (new_date, product, price))
    conn.commit()
    
def leitura_todos_dados():
    cur.execute("SELECT * FROM produtos")
    for linha in cur.fetchall():
        print(linha)
        
def leitura_registros():
    cur.execute('SELECT * FROM produtos WHERE valor > 60.0')
    for linha in cur.fetchall():
        print(linha)
        
def leitura_colunas():
    cur.execute("SELECT * FROM produtos")
    for linha in cur.fetchall():
        print(linha[3])
        
def atualiza_dados():
    cur.execute('UPDATE produtos SET valor = 100.00 WHERE valor = 90.00')
    conn.commit()
    
def remove_dados():
    cur.execute('DELETE from produtos WHERE valor = 519.00')
    conn.commit()


# In[6]:


create_table()


# In[3]:


data_insert()


# In[4]:


for i in range(10):
    data_insert_var()
    time.sleep(1)


# In[19]:


cur.close()
conn.close()


# # Consultas no BD

# In[7]:


leitura_todos_dados()


# In[8]:


leitura_registros()


# In[9]:


leitura_colunas()


# # Update e delete

# In[7]:


atualiza_dados()


# In[8]:


remove_dados()


# In[ ]:




