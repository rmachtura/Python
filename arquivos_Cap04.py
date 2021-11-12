#!/usr/bin/env python
# coding: utf-8

# # Arquivos

# In[7]:


#r é de read de leitura
arq1 = open("arquivos/arquivo1.txt", "r")


# In[8]:


print(arq1.read())


# In[6]:


#Numero de caracteres
print(arq1.tell())


# In[9]:


print(arq1.seek(0,0))


# In[10]:


print(arq1.read(10))


# # Gravando arquivo

# In[11]:


#o w é para write de escrita, ele sobrescreve
arq2 = open('arquivos/arquivo1.txt', 'w')


# In[12]:


print(arq2.read())


# In[13]:


arq2.write("Gravação de arquivos Python")


# In[14]:


arq2 = open('arquivos/arquivo1.txt', 'r')


# In[15]:


print(arq2.read())


# In[16]:


#Para acrescentar conteúdo e não sobreescrever usar a de append
arq2 = open('arquivos/arquivo1.txt', 'a')


# In[17]:


arq2.write("Acrescentando conteudo")


# In[20]:


arq2.close()


# In[21]:


arq2 = open('arquivos/arquivo1.txt', 'r')


# In[22]:


print(arq2.read())


# #Automatizando o nome do arquivo para criação

# In[23]:


fileName = input("Digite o nome do arquivo:")


# In[24]:


fileName = fileName + ".txt"


# In[26]:


arq3 = open(fileName, "w")


# In[28]:


arq3.write("Incluindo texto no arquivo criado")


# In[29]:


arq3.close()


# In[30]:


arq3 = open(fileName, "r")


# In[31]:


print(arq3.read())


# In[32]:


arq3.close()


# ## DataSets

# In[33]:


f = open("arquivos/salarios.csv", 'r')


# In[34]:


data = f.read()


# In[35]:


rows = data.split('\n')


# In[36]:


print(rows)


# In[37]:


f = open("arquivos/salarios.csv", 'r')


# In[44]:


data = f.read()


# In[45]:


rows = data.split('\n')


# In[46]:


full_data = []


# In[47]:


for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)


# In[48]:


print(full_data)


# In[49]:


f = open("arquivos/salarios.csv", 'r')


# In[50]:


data = f.read()


# In[51]:


rows = data.split('\n')


# In[52]:


full_data = []


# In[53]:


for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)


# In[55]:


count = 0
for row in full_data:
    count += 1


# In[56]:


print(count)


# In[57]:


f = open("arquivos/salarios.csv", 'r')


# In[58]:


data = f.read()
rows = data.split('\n')
full_data = []


# In[59]:


for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
    first_row = full_data[0]
count = 0


# In[60]:


for column in first_row:
    count += 1


# In[61]:


print(count)


# # #Arquivos pelo Jupyter notebook

# In[1]:


get_ipython().run_cell_magic('writefile', 'arquivos/teste_jupyter.txt', 'Olá este arquivo foi gerado pelo próprio Jupyter notebook.\nPodemos gerar quantas linhas quisermos.')


# In[2]:


arq4 = open("arquivos/teste_jupyter.txt")


# In[3]:


arq4.read()


# In[5]:


arq4.read()


# In[6]:


arq4.seek(0)


# In[7]:


arq4.read()


# In[8]:


arq4.seek(0)


# In[11]:


arq4.seek(0)
arq4.readlines()


# In[12]:


#Usar readlines ou um for
for line in open("arquivos/teste_jupyter.txt"):
    print(line)


# # #Importando datasets com Pandas

# In[13]:


import pandas as pd


# In[14]:


file_name = "arquivos/binary.csv"


# In[15]:


df = pd.read_csv(file_name)


# In[16]:


df.head()


# In[17]:


file2 = "arquivos/salarios.csv"


# In[18]:


df2 = pd.read_csv(file2)


# In[19]:


df2.head()


# In[20]:





# # #arquivos txt

# In[21]:


texto = "Cientista de dados eh a profissao que mais tem crescido no mundo. \n"
texto = texto + "Esses profissionais precisam se especializar em Programacao, estatistica e machine learning"
texto += "E claro, Big Data"


# In[22]:


print(texto)


# In[23]:


import os


# In[24]:


arquivo = open(os.path.join('arquivos/cientista.txt'), 'w')


# In[25]:


for palavra in texto.split():
    arquivo.write(palavra+ ' ')


# In[26]:


arquivo.close()


# In[27]:


arquivo = open('arquivos/cientista.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)


# In[28]:


#Expressão with
with open('arquivos/cientista.txt', 'r') as arquivo:
    conteudo = arquivo.read()


# In[29]:


print(len(conteudo))


# In[30]:


print(conteudo)


# In[31]:


with open('arquivos/cientista.txt', 'w') as arquivo:
    arquivo.write(texto[:21])
    arquivo.write('\n')
    arquivo.write(texto[:33])


# In[32]:


arquivo = open('arquivos/cientista.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)


# ## Arquivos CSV

# In[1]:


import csv


# In[2]:


with open('arquivos/numeros.csv', 'w') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(('primeira', 'segunda', 'terceira'))
    writer.writerow((55,93,68))
    writer.writerow((62,14,86))


# In[3]:


with open('arquivos/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print('Número de colunas: ', len(x))
        print(x)


# In[5]:


with open('arquivos/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)
    
    print(dados)


# In[10]:


for linha in dados[:1]:
    print(linha)


# ## Arquivos JSON 

# In[11]:


#Dicionario
dict = {'nome':'Guido Van Rossum',
        'linguagem':'Python',
        'similar':['c', 'Modula-3', 'lisp'],
       'users':10000}


# In[12]:


import json


# In[13]:


#Converte dicionario em JSON
json.dumps(dict)


# In[14]:


with open('arquivos/dados.json', 'w') as arquivo:
    arquivo.write(json.dumps(dict))


# In[15]:


with open('arquivos/dados.json', 'r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)


# In[16]:


print(data)


# In[17]:


print(data['nome'])


# In[18]:


from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
data = json.loads(response)[0]


# In[19]:


print("Titulo: ", data['title'])
print("URL: ", data['url'])
print("Duração: ", data['duration'])
print("Numero de visualizações: ", data['stats_number_of_plays'])


# In[20]:


import os
arquivo_fonte = 'arquivos/dados.json'
arquivo_destino = 'arquivos/json_data.txt'


# In[22]:


with open(arquivo_fonte, 'r') as infile:
    text = infile.read()
    with open(arquivo_destino, 'w') as outfile:
        outfile.write(text)


# In[23]:


open(arquivo_destino, 'w').write(open(arquivo_fonte, 'r').read())


# In[24]:


with open('arquivos/json_data.txt', 'r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)


# In[25]:


print(data)


# In[ ]:




